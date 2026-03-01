import openai
import json
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()


class NewsAnalyzer:
    """Poe APIを使ってニュースを分析・要約するクラス"""

    def __init__(self):
        # Poe API設定
        self.client = openai.OpenAI(
            api_key=os.getenv("POE_API_KEY"),
            base_url="https://api.poe.com/v1",
        )
        self.model = os.getenv("POE_MODEL", "gemini-3-flash")

        print(f"🤖 LLMモデル: {self.model}")

    def translate_to_japanese(self, text: str) -> str:
        """
        英語のテキストを日本語に翻訳

        Args:
            text: 翻訳するテキスト

        Returns:
            翻訳されたテキスト（失敗時は元のテキスト）
        """
        if not text or len(text.strip()) == 0:
            return text

        # 既に日本語が含まれている場合はスキップ（簡易チェック）
        japanese_chars = len([c for c in text if '\u3040' <= c <= '\u30ff' or '\u4e00' <= c <= '\u9faf'])
        if japanese_chars > len(text) * 0.3:  # 30%以上が日本語文字
            return text

        prompt = f"""以下の英語テキストを自然な日本語に翻訳してください。
翻訳結果のみを出力し、説明や追加のテキストは不要です。

英語テキスト:
{text}

日本語訳:"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "あなたは英語から日本語への翻訳の専門家です。自然で読みやすい日本語に翻訳してください。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1000
            )

            translated = response.choices[0].message.content.strip()
            return translated

        except Exception as e:
            print(f"  ⚠️  翻訳エラー: {str(e)}")
            return text

    def evaluate_article_importance(self, article: Dict) -> int:
        """
        記事の重要度を評価（1-5の星評価）

        Args:
            article: 記事の辞書

        Returns:
            重要度スコア（1-5）、エラー時は0
        """
        # summaryが文字列であることを確認
        summary = article.get('summary', '')
        if isinstance(summary, list):
            summary = ' '.join(summary)
        summary = str(summary)[:300]

        prompt = f"""あなたは車とIT業界の専門アナリストです。以下の記事の重要度を星5段階で評価してください。

記事タイトル: {article['title']}
記事概要: {summary}
情報源: {article['source']}

評価基準:
★★★★★ (5): 業界を変える革新的発表（新型車の正式発表、画期的技術、業界再編など）
★★★★☆ (4): 非常に重要なニュース（大手企業の戦略発表、重要な技術革新など）
★★★☆☆ (3): 注目すべきニュース（新製品、業界動向、トレンドなど）
★★☆☆☆ (2): 一般的なニュース（通常のアップデート、小規模発表など）
★☆☆☆☆ (1): あまり重要でないニュース（マイナーな更新、個人の意見など）

**重要**: 必ず日本語でJSON形式で回答してください:
{{
    "score": 1-5の数値,
    "reason": "評価理由を日本語で簡潔に（30文字以内）"
}}"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "あなたは業界ニュースの重要度を評価する専門家です。必ず日本語でJSON形式で回答してください。英語は一切使用しないでください。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=150
            )

            content = response.choices[0].message.content

            # JSONブロックを抽出
            if "```json" in content:
                json_str = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                json_str = content.split("```")[1].split("```")[0].strip()
            else:
                json_str = content.strip()

            result = json.loads(json_str)
            score = result.get("score", 0)

            # 星マークで表示
            stars = "★" * score + "☆" * (5 - score)
            print(f"  {stars} ({score}/5) - {article['title'][:50]}...")

            return score

        except Exception as e:
            print(f"  ⚠️  重要度評価エラー: {str(e)}")
            return 0

    def summarize_daily_news(self, articles: List[Dict], importance_threshold: int = 3) -> str:
        """
        ニュース記事をまとめて要約（重要度基準で選択）

        Args:
            articles: 記事のリスト
            importance_threshold: 重要度の閾値（1-5、この値以上の記事のみ配信）

        Returns:
            要約されたニュース文字列
        """
        if not articles:
            return "本日は新しいニュースがありませんでした。"

        threshold_stars = "★" * importance_threshold + "☆" * (5 - importance_threshold)
        print(f"🔍 記事の重要度を評価中（閾値: {threshold_stars} {importance_threshold}/5）...\n")

        # 各記事の重要度を評価
        all_scored_articles = []
        for article in articles[:30]:  # 最大30件を評価
            score = self.evaluate_article_importance(article)
            article['importance_score'] = score
            all_scored_articles.append(article)

        # 重要度順にソート
        all_scored_articles.sort(key=lambda x: x.get('importance_score', 0), reverse=True)

        # 重要記事（★3以上）と一般記事（★1-2）に分類
        important_articles = [a for a in all_scored_articles if a.get('importance_score', 0) >= importance_threshold]
        minor_articles = [a for a in all_scored_articles if a.get('importance_score', 0) < importance_threshold and a.get('importance_score', 0) > 0]

        if not important_articles and not minor_articles:
            return f"本日は評価可能なニュースがありませんでした。"

        print(f"\n✅ 重要記事: {len(important_articles)} 件")
        print(f"   その他記事: {len(minor_articles)} 件\n")

        # 重要記事の詳細情報を整形
        important_articles_text = ""
        if important_articles:
            for i, article in enumerate(important_articles, 1):
                score = article.get('importance_score', 0)
                stars = "★" * score + "☆" * (5 - score)
                important_articles_text += f"""
記事{i}:
タイトル: {article['title']}
概要: {article['summary'][:200]}
ソース: {article['source']}
重要度: {stars} ({score}/5)
---
"""

        # 一般記事のリスト
        minor_articles_text = ""
        if minor_articles:
            minor_articles_text = "\n\n### その他の記事（★1-2）:\n"
            for article in minor_articles[:10]:
                score = article.get('importance_score', 0)
                stars = "★" * score + "☆" * (5 - score)
                minor_articles_text += f"- {stars} {article['title'][:60]}... ({article['source']})\n"

        # 重要記事がある場合のみLLMで要約
        if important_articles:
            prompt = f"""あなたは車とITに特化したニュースキュレーターです。
以下の重要度の高い記事を日本語で要約してください。各記事は既に重要度 {threshold_stars} ({importance_threshold}/5) 以上と評価されています。

**重要**: 必ず日本語のみで回答してください。英語は一切使用しないでください。

出力フォーマット:
## 🚗💻 今日の注目ニュース

**1. [カテゴリ] タイトル**
• 要点を簡潔に要約
• なぜ重要かの説明

{important_articles_text}"""

            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "あなたは車とIT業界に詳しい専門ニュースキュレーターです。必ず日本語のみで回答してください。英語は一切使用しないでください。"},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=3000,
                    temperature=0.3
                )

                summary = response.choices[0].message.content

                # 一般記事のリストを追加
                if minor_articles_text:
                    summary += minor_articles_text

                # システム側で記事URLリストを追加
                summary = self._append_article_urls(summary, important_articles, len(important_articles))

                return summary

            except Exception as e:
                return f"⚠️ 要約処理でエラーが発生しました: {str(e)}"
        else:
            # 重要記事がない場合は一般記事のリストのみ
            return f"本日は重要度 {threshold_stars} ({importance_threshold}/5) 以上のニュースがありませんでした。{minor_articles_text}"

    def _append_article_urls(self, summary: str, articles: List[Dict], max_count: int) -> str:
        """
        要約の最後に記事URLのリストを追加

        Args:
            summary: LLMが生成した要約テキスト
            articles: 記事のリスト
            max_count: 表示する最大記事数

        Returns:
            URLリストが追加された要約テキスト
        """
        url_section = "\n\n---\n\n## 📎 記事リンク\n\n"

        for i, article in enumerate(articles[:max_count], 1):
            url_section += f"{i}. [{article['title'][:80]}...]({article['url']}) - *{article['source']}*\n"

        return summary + url_section

    def detect_new_car_announcement(self, article: Dict) -> Optional[Dict]:
        """
        記事が新型車の発表かどうかを判定

        Args:
            article: 記事の辞書

        Returns:
            新型車情報の辞書、または None
        """
        # summaryが文字列であることを確認
        summary = article.get('summary', '')
        if isinstance(summary, list):
            summary = ' '.join(summary)
        summary = str(summary)[:500]

        prompt = f"""あなたは自動車業界の専門アナリストです。以下の記事を分析し、新型車・プロトタイプ・コンセプトカーの発表に関するものかどうか判定してください。

記事タイトル: {article['title']}
記事概要: {summary}
情報源: {article['source']}

判定基準:
✅ 含めるべき内容:
- 完全新型モデルの発表
- フルモデルチェンジ
- マイナーチェンジ・フェイスリフト
- コンセプトカーの公開
- プロトタイプ・テスト車両の目撃
- 特別仕様車・限定モデル

❌ 除外すべき内容:
- 単純な販売開始・価格発表（新型でない場合）
- 決算・業績発表
- 人事異動
- リコール情報
- レース結果

**重要**: 必ず日本語でJSON形式で回答してください。英語は一切使用しないでください:
{{
    "is_new_car": true か false,
    "confidence": 0-100の数値,
    "manufacturer": "メーカー名を日本語で（不明なら「不明」）",
    "model_name": "モデル名（不明なら「不明」）",
    "category": "SUV/セダン/ハッチバック/スポーツ/トラック/EV/コンセプト/不明",
    "announcement_type": "Official_Debut/Facelift/Concept/Prototype/Limited_Edition/Unknown",
    "importance": 1-10の数値,
    "summary_ja": "新型車の場合のみ、この車を日本語で一言で説明（50文字以内）"
}}"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "あなたは自動車業界に精通した専門アナリストです。必ず日本語でJSON形式で回答してください。英語は一切使用しないでください。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1
            )

            # レスポンスからJSONを抽出
            content = response.choices[0].message.content

            # JSONブロックを探す
            if "```json" in content:
                json_str = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                json_str = content.split("```")[1].split("```")[0].strip()
            else:
                json_str = content.strip()

            result = json.loads(json_str)

            # 新型車と判定され、信頼度が70%以上の場合のみ返す
            if result.get("is_new_car") and result.get("confidence", 0) >= 70:
                return {
                    **result,
                    'original_article': article
                }

            return None

        except json.JSONDecodeError as e:
            print(f"  ⚠️  JSON解析エラー: {str(e)}")
            return None
        except Exception as e:
            print(f"  ⚠️  新型車判定エラー: {str(e)}")
            return None

    def analyze_all_for_new_cars(self, articles: List[Dict]) -> List[Dict]:
        """
        全記事を分析して新型車情報を抽出

        Args:
            articles: 記事のリスト

        Returns:
            新型車情報のリスト
        """
        new_cars = []

        print("🔍 新型車情報を検索中...")

        for i, article in enumerate(articles, 1):
            print(f"  分析中 {i}/{len(articles)}: {article['title'][:50]}...")

            result = self.detect_new_car_announcement(article)

            if result:
                new_cars.append(result)
                print(f"    ✅ 新型車発見: {result['manufacturer']} {result['model_name']}")

        print(f"\n🚗 {len(new_cars)} 件の新型車情報を発見しました\n")

        return new_cars
