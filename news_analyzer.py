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
        # 重要度評価・要約用のモデル（翻訳より判断力が必要なため別に指定できる）
        self.scoring_model = os.getenv("POE_SCORING_MODEL") or self.model

        print(f"🤖 LLMモデル: {self.model}（評価・要約: {self.scoring_model}）")

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

    def _ask_json(self, system: str, prompt: str, max_tokens: int) -> Dict:
        """
        評価用モデルにJSONで回答させて解析する。
        失敗した場合は翻訳用モデル（POE_MODEL）でもう一度試す。

        Raises:
            ValueError: どちらのモデルでも解析できなかった場合
        """
        models = [self.scoring_model]
        if self.model != self.scoring_model:
            models.append(self.model)

        last_error = None
        for model in models:
            content = ""
            try:
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.2,
                    max_tokens=max_tokens
                )
                content = response.choices[0].message.content or ""
                return self._parse_json(content)
            except Exception as e:
                last_error = e
                print(f"  ⚠️  {model} の回答を解析できませんでした: {str(e)} / 回答: {content[:80]!r}")

        raise ValueError(f"JSONを取得できませんでした: {last_error}")

    @staticmethod
    def _parse_json(content: str) -> Dict:
        """回答テキストからJSONオブジェクトを取り出す（前後の文章やコードブロックは無視する）"""
        start = content.find("{")
        end = content.rfind("}")
        if start == -1 or end < start:
            raise ValueError("回答にJSONが含まれていません")
        return json.loads(content[start:end + 1])

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

評価基準（厳しく評価すること。1日100件の記事のうち★4以上は数件、★5は月に数件しかない想定）:
★★★★★ (5): 業界の歴史に残る出来事（主要メーカーの重要な新型車の世界初公開、大型買収・業界再編、AIなど基盤技術の画期的なブレークスルー）
★★★★☆ (4): 業界全体に影響する重要ニュース（大手企業の大きな戦略転換、主要な新製品・新モデルの正式発表、重大なリコール・規制・セキュリティ事件）
★★★☆☆ (3): 業界関係者なら知っておきたいニュース（大手の新製品・新サービス、市場動向の数字、注目企業の資金調達）
★★☆☆☆ (2): 一般的なニュース（既存製品のアップデート、小規模企業の発表、イベント告知、試乗記・レビュー）
★☆☆☆☆ (1): 個人ブログ・技術メモ・How-to記事、エラー解決方法、コラム・意見記事、セール情報、マイナーな更新

迷ったら低い方の点数を付けてください。Qiita・Zenn・DevelopersIOなどの技術記事は、原則★1〜2です。

**重要**: 必ず日本語でJSON形式で回答してください:
{{
    "score": 1-5の数値,
    "reason": "評価理由を日本語で簡潔に（30文字以内）"
}}"""

        try:
            result = self._ask_json(
                "あなたは業界ニュースの重要度を評価する専門家です。必ず日本語でJSON形式で回答してください。英語は一切使用しないでください。",
                prompt,
                max_tokens=1000
            )
            score = int(result.get("score", 0))
            if not 1 <= score <= 5:
                raise ValueError(f"スコアが範囲外です: {score}")

            # 星マークで表示
            stars = "★" * score + "☆" * (5 - score)
            print(f"  {stars} ({score}/5) - {article['title'][:50]}...")

            return score

        except Exception as e:
            print(f"  ⚠️  重要度評価エラー: {str(e)}")
            return 0

    def _select_articles_for_evaluation(self, articles: List[Dict], max_count: int) -> List[Dict]:
        """
        評価対象の記事を情報源ごとに順番に選ぶ（1つの情報源に偏らないようにする）

        Args:
            articles: 記事のリスト（新しい順）
            max_count: 選ぶ最大記事数

        Returns:
            選ばれた記事のリスト
        """
        by_source = {}
        for article in articles:
            by_source.setdefault(article['source'], []).append(article)

        selected = []
        queues = list(by_source.values())
        while len(selected) < max_count and queues:
            for queue in queues:
                if len(selected) >= max_count:
                    break
                selected.append(queue.pop(0))
            queues = [q for q in queues if q]

        return selected

    def _rerank_top_articles(self, articles: List[Dict], max_top: int, top_threshold: int = 4) -> None:
        """
        ★4以上の記事をまとめてLLMに比較させ、本当に重要な上位max_top件だけを残す
        （個別評価では★4が乱発されるため）。選ばれなかった記事は★3に下げる。

        Args:
            articles: importance_score付きの記事のリスト（その場で書き換える）
            max_top: ★4以上として残す最大記事数
            top_threshold: 相対評価の対象にする重要度
        """
        candidates = [a for a in articles if a.get('importance_score', 0) >= top_threshold]
        if len(candidates) <= max_top:
            return

        print(f"\n⚖️  ★{top_threshold}以上の {len(candidates)} 件を比較して上位 {max_top} 件に絞り込み中...\n")

        article_list = ""
        for i, article in enumerate(candidates, 1):
            summary = article.get('summary', '')
            if isinstance(summary, list):
                summary = ' '.join(summary)
            article_list += f"{i}. {article['title']}（{article['source']}）\n   {str(summary)[:120]}\n"

        prompt = f"""あなたは車とIT業界の専門アナリストです。以下は今日のニュース候補です。
この中から、業界関係者が今日必ず知っておくべき最も重要なニュースを最大{max_top}件選んでください。

選ぶ基準:
- 業界全体に影響する事実（正式発表、大型提携・買収、重大なリコール・規制・情報漏えいなど）を優先する
- 同じ出来事を扱った記事が複数ある場合は、最も情報量の多い1件だけを選ぶ
- コラム・意見記事・ポッドキャスト・試乗記・レビュー・写真ギャラリー・噂や予想は選ばない
- 該当するものが少なければ{max_top}件未満でもよい

候補:
{article_list}
**重要**: 次のJSON形式のみで回答してください（重要な順に番号を並べる）:
{{"top": [番号, 番号, ...]}}"""

        try:
            result = self._ask_json(
                "あなたは業界ニュースの重要度を比較評価する専門家です。必ずJSON形式で回答してください。",
                prompt,
                max_tokens=1000
            )

            top_numbers = result.get("top", [])
            selected_ids = set()
            for n in top_numbers:
                if isinstance(n, int) and 1 <= n <= len(candidates) and len(selected_ids) < max_top:
                    selected_ids.add(id(candidates[n - 1]))

        except Exception as e:
            print(f"  ⚠️  相対評価エラー: {str(e)}（個別評価のスコアをそのまま使います）")
            return

        for article in candidates:
            if id(article) in selected_ids:
                print(f"  ✅ ★{article['importance_score']} 維持 - {article['title'][:50]}...")
            else:
                article['importance_score'] = top_threshold - 1

        print(f"\n  → ★{top_threshold}以上: {len(candidates)} 件 → {len(selected_ids)} 件\n")

    def summarize_daily_news(self, articles: List[Dict], importance_threshold: int = 3, max_evaluate: int = 80, max_top: int = 5) -> str:
        """
        ニュース記事をまとめて要約（重要度基準で選択）

        Args:
            articles: 記事のリスト
            importance_threshold: 重要度の閾値（1-5、この値以上の記事のみ配信）
            max_evaluate: 重要度を評価する最大記事数
            max_top: ★4以上として残す最大記事数（相対評価で絞り込む）

        Returns:
            要約されたニュース文字列
        """
        if not articles:
            return "本日は新しいニュースがありませんでした。"

        threshold_stars = "★" * importance_threshold + "☆" * (5 - importance_threshold)
        print(f"🔍 記事の重要度を評価中（閾値: {threshold_stars} {importance_threshold}/5）...\n")

        # 各記事の重要度を評価
        all_scored_articles = []
        for article in self._select_articles_for_evaluation(articles, max_evaluate):
            score = self.evaluate_article_importance(article)
            article['importance_score'] = score
            all_scored_articles.append(article)

        # ★4以上の記事を相対評価で上位数件に絞る
        self._rerank_top_articles(all_scored_articles, max_top)

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
                    model=self.scoring_model,
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
