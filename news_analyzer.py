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

    def summarize_daily_news(self, articles: List[Dict], max_articles: int = 10) -> str:
        """
        ニュース記事をまとめて要約

        Args:
            articles: 記事のリスト
            max_articles: 要約する最大記事数

        Returns:
            要約されたニュース文字列
        """
        if not articles:
            return "本日は新しいニュースがありませんでした。"

        # 記事リストを保持
        article_list = articles[:20]

        # 記事を整形（URLは含めない）
        articles_text = ""
        for i, article in enumerate(article_list, 1):
            articles_text += f"""
記事{i}:
タイトル: {article['title']}
概要: {article['summary'][:200]}
ソース: {article['source']}
---
"""

        prompt = f"""あなたは車とITに特化したニュースキュレーターです。
以下の記事から、読者にとって最も価値のあるニュース{max_articles}件を選び、要約してください。

選考基準:
- 技術的革新性や業界への影響度
- 一般読者の関心度
- 車とITの分野に関連性が高いもの
- 新型車・新製品の発表は特に重視

出力フォーマット:
## 🚗💻 今日の注目ニュース

**[カテゴリ] タイトル**
• 要点を簡潔に要約
• なぜ重要かの説明

{articles_text}"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "あなたは車とIT業界に詳しい専門ニュースキュレーターです。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.3
            )

            summary = response.choices[0].message.content

            # システム側で記事URLリストを追加
            summary = self._append_article_urls(summary, article_list, max_articles)

            return summary

        except Exception as e:
            return f"⚠️ 要約処理でエラーが発生しました: {str(e)}"

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
        prompt = f"""あなたは自動車業界の専門アナリストです。以下の記事を分析し、新型車・プロトタイプ・コンセプトカーの発表に関するものかどうか判定してください。

記事タイトル: {article['title']}
記事概要: {article['summary'][:500]}
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

以下のJSON形式で回答してください:
{{
    "is_new_car": true か false,
    "confidence": 0-100の数値,
    "manufacturer": "メーカー名（不明ならUnknown）",
    "model_name": "モデル名（不明ならUnknown）",
    "category": "SUV/Sedan/Hatchback/Sports/Truck/EV/Concept/Unknown",
    "announcement_type": "Official_Debut/Facelift/Concept/Prototype/Limited_Edition/Unknown",
    "importance": 1-10の数値,
    "summary_ja": "新型車の場合のみ、この車を一言で説明（50文字以内）"
}}"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "あなたは自動車業界に精通した専門アナリストです。必ずJSON形式で回答してください。"},
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
