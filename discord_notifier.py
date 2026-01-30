import requests
from typing import List, Dict, Optional
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


class DiscordNotifier:
    """Discord Webhookを使ってニュースを配信するクラス"""

    def __init__(self):
        # 3つの異なるWebhook URL
        self.it_webhook_url = os.getenv("IT_WEBHOOK_URL")
        self.car_webhook_url = os.getenv("CAR_WEBHOOK_URL")
        self.new_car_webhook_url = os.getenv("NEW_CAR_WEBHOOK_URL")

        # 後方互換性のため、古い設定もサポート
        default_webhook = os.getenv("DISCORD_WEBHOOK_URL")

        if not self.it_webhook_url:
            self.it_webhook_url = default_webhook
        if not self.car_webhook_url:
            self.car_webhook_url = default_webhook
        if not self.new_car_webhook_url:
            self.new_car_webhook_url = default_webhook

        if not any([self.it_webhook_url, self.car_webhook_url, self.new_car_webhook_url]):
            raise ValueError("少なくとも1つのWebhook URLを設定してください")

        print(f"🔔 Discord設定:")
        print(f"   - ITチャンネル: {'✅' if self.it_webhook_url else '❌'}")
        print(f"   - 車チャンネル: {'✅' if self.car_webhook_url else '❌'}")
        print(f"   - 新車チャンネル: {'✅' if self.new_car_webhook_url else '❌'}")

        # 発表タイプ別の色分け
        self.color_scheme = {
            'Official_Debut': 0xFF0000,    # 赤 - 正式発表（最重要）
            'Facelift': 0xFF6600,          # オレンジ - マイナーチェンジ
            'Concept': 0x0066FF,           # 青 - コンセプトカー
            'Prototype': 0x9900FF,         # 紫 - プロトタイプ
            'Limited_Edition': 0xFFD700,   # 金 - 限定モデル
            'Unknown': 0x00FF00,           # 緑 - その他
        }

    def send_daily_summary(self, summary_text: str, articles: list = None, category: str = None) -> bool:
        """
        日次ニュースサマリーをEmbed形式で送信

        Args:
            summary_text: 要約されたニューステキスト
            articles: 記事のリスト（URLリンク用）
            category: 'it', 'car', またはNone（すべて）

        Returns:
            送信成功したかどうか
        """
        import time
        import re

        # カテゴリに応じたWebhook URLを選択
        webhook_url = self._get_webhook_for_category(category)
        if not webhook_url:
            print(f"⚠️ カテゴリ '{category}' のWebhook URLが設定されていません")
            return False

        # ヘッダーメッセージを送信
        category_emoji = "💻" if category == "it" else "🚗" if category == "car" else "🚗💻"
        category_name = "IT" if category == "it" else "車" if category == "car" else "総合"
        header = f"## {category_emoji} 今日の{category_name}ニュース ({datetime.now().strftime('%Y年%m月%d日')})"
        self._send_message(header, webhook_url)
        time.sleep(0.5)

        # ニュースを個別に抽出してEmbed送信
        news_items = self._parse_news_items(summary_text)

        for i, item in enumerate(news_items, 1):
            if i > 1:
                time.sleep(1)  # レート制限対策

            success = self._send_news_embed(item, i, webhook_url)
            if not success:
                print(f"⚠️ ニュース {i}/{len(news_items)} の送信に失敗しました")
                return False
            else:
                print(f"✅ ニュース {i}/{len(news_items)} を送信しました")

        # 記事リンクセクションを送信
        if articles:
            time.sleep(1)
            links_section = self._create_links_section(articles)
            self._send_message(links_section, webhook_url)

        return True

    def send_articles_by_category(self, articles: List[Dict]) -> bool:
        """
        記事をカテゴリ別に分類して適切なチャンネルに送信

        Args:
            articles: 記事のリスト

        Returns:
            送信成功したかどうか
        """
        import time

        # カテゴリ別に記事を分類
        it_articles = [a for a in articles if a.get('category') == 'it']
        car_articles = [a for a in articles if a.get('category') == 'car']

        success = True

        # IT記事を送信
        if it_articles:
            print(f"\n📤 IT記事 {len(it_articles)} 件を送信中...")
            # LLMで要約を生成する必要があるため、main.pyから呼び出す
            # ここでは記事リストのみを返す
            pass

        # 車記事を送信
        if car_articles:
            print(f"\n📤 車記事 {len(car_articles)} 件を送信中...")
            pass

        return success

    def send_new_car_alert(self, car_info: Dict) -> bool:
        """
        新型車情報をリッチな形式で送信（専用チャンネルへ）

        Args:
            car_info: 新型車の情報辞書

        Returns:
            送信成功したかどうか
        """
        article = car_info.get('original_article', {})

        # 重要度に応じた絵文字
        importance = car_info.get('importance', 5)
        importance_emoji = "🔥" * min(importance, 5)

        # 埋め込みメッセージの作成
        embed = {
            "title": f"🚨 {car_info['manufacturer']} {car_info['model_name']} 登場！",
            "description": car_info.get('summary_ja', '新型車が発表されました'),
            "url": article.get('url', ''),
            "color": self.color_scheme.get(car_info['announcement_type'], 0x00FF00),
            "timestamp": datetime.now().isoformat(),
            "fields": [
                {
                    "name": "🏭 メーカー",
                    "value": car_info['manufacturer'],
                    "inline": True
                },
                {
                    "name": "🚗 カテゴリ",
                    "value": car_info['category'],
                    "inline": True
                },
                {
                    "name": "📍 発表タイプ",
                    "value": car_info['announcement_type'].replace('_', ' '),
                    "inline": True
                },
                {
                    "name": f"⭐ 重要度 ({importance}/10)",
                    "value": importance_emoji,
                    "inline": True
                },
                {
                    "name": "📰 情報源",
                    "value": article.get('source', 'Unknown'),
                    "inline": True
                },
                {
                    "name": "🔗 記事リンク",
                    "value": f"[記事を読む]({article.get('url', '#')})",
                    "inline": False
                }
            ],
            "footer": {
                "text": f"信頼度: {car_info.get('confidence', 0)}% | Auto News Tracker"
            }
        }

        payload = {
            "content": "🚗 **新型車情報をキャッチしました！**",
            "embeds": [embed]
        }

        # 新型車専用チャンネルに送信
        return self._send_webhook(payload, self.new_car_webhook_url)

    def send_new_car_summary(self, new_cars: List[Dict]) -> bool:
        """
        複数の新型車情報をまとめて送信

        Args:
            new_cars: 新型車情報のリスト

        Returns:
            送信成功したかどうか
        """
        if not new_cars:
            return True

        # 重要度順にソート
        sorted_cars = sorted(new_cars, key=lambda x: x.get('importance', 0), reverse=True)

        content = f"## 🚨 本日の新型車情報 ({len(new_cars)}件)\n\n"

        for i, car in enumerate(sorted_cars, 1):
            article = car.get('original_article', {})
            importance_emoji = "⭐" * min(car.get('importance', 5), 5)

            content += f"**{i}. {car['manufacturer']} {car['model_name']}**\n"
            content += f"• {car.get('summary_ja', '詳細情報なし')}\n"
            content += f"• カテゴリ: {car['category']} | タイプ: {car['announcement_type']}\n"
            content += f"• 重要度: {importance_emoji}\n"
            content += f"• [記事を読む]({article.get('url', '#')})\n\n"

        return self.send_daily_summary(content)

    def _send_message(self, content: str, webhook_url: str = None) -> bool:
        """シンプルなテキストメッセージを送信"""
        payload = {"content": content}
        return self._send_webhook(payload, webhook_url)

    def _send_webhook(self, payload: Dict, webhook_url: str = None) -> bool:
        """Webhookにペイロードを送信"""
        # デフォルトはITチャンネル（後方互換性のため）
        if not webhook_url:
            webhook_url = self.it_webhook_url or self.car_webhook_url

        if not webhook_url:
            print(f"❌ Webhook URLが設定されていません")
            return False

        try:
            response = requests.post(webhook_url, json=payload)

            if response.status_code in [200, 204]:
                return True
            else:
                print(f"❌ Discord送信失敗: ステータスコード {response.status_code}")
                return False

        except Exception as e:
            print(f"❌ Discord送信エラー: {str(e)}")
            return False

    def _get_webhook_for_category(self, category: Optional[str]) -> Optional[str]:
        """
        カテゴリに応じた適切なWebhook URLを返す

        Args:
            category: 'it', 'car', またはNone

        Returns:
            Webhook URL
        """
        if category == 'it':
            return self.it_webhook_url
        elif category == 'car':
            return self.car_webhook_url
        else:
            # デフォルトは車チャンネル
            return self.car_webhook_url or self.it_webhook_url

    def _split_text(self, text: str, max_length: int) -> List[str]:
        """長いテキストを適切な位置で分割"""
        chunks = []
        current_chunk = ""

        # 記事の区切り（## や --- など）を優先的に分割ポイントにする
        lines = text.split('\n')

        for i, line in enumerate(lines):
            # 次の行を追加すると制限を超える場合
            if len(current_chunk) + len(line) + 1 > max_length:
                # 現在のチャンクを保存
                if current_chunk:
                    chunks.append(current_chunk.rstrip())
                # 新しいチャンクを開始
                current_chunk = line + '\n'
            else:
                current_chunk += line + '\n'

        # 最後のチャンクを追加
        if current_chunk:
            chunks.append(current_chunk.rstrip())

        return chunks

    def test_connection(self) -> bool:
        """接続テスト（すべてのチャンネルをテスト）"""
        import time
        success = True

        if self.it_webhook_url:
            print("💻 ITチャンネルをテスト中...")
            success &= self._send_message("✅ ITチャンネル接続テストに成功しました！", self.it_webhook_url)
            time.sleep(1)

        if self.car_webhook_url:
            print("🚗 車チャンネルをテスト中...")
            success &= self._send_message("✅ 車チャンネル接続テストに成功しました！", self.car_webhook_url)
            time.sleep(1)

        if self.new_car_webhook_url:
            print("🚨 新車チャンネルをテスト中...")
            success &= self._send_message("✅ 新車チャンネル接続テストに成功しました！", self.new_car_webhook_url)

        return success

    def _parse_news_items(self, summary_text: str) -> List[Dict]:
        """
        要約テキストから個別のニュース項目を抽出

        Args:
            summary_text: LLMが生成した要約テキスト

        Returns:
            ニュース項目のリスト
        """
        import re

        items = []
        lines = summary_text.split('\n')

        current_item = None
        for line in lines:
            # ニュースの開始を検出（**で始まる行）
            if line.strip().startswith('**') and '[' in line:
                # 前のアイテムを保存
                if current_item:
                    items.append(current_item)

                # 新しいアイテムを開始
                # **1. [カテゴリ] タイトル** のようなパターン
                match = re.match(r'\*\*\d+\.\s*\[([^\]]+)\]\s*([^*]+)\*\*', line)
                if match:
                    category = match.group(1)
                    title = match.group(2).strip()
                    current_item = {
                        'category': category,
                        'title': title,
                        'description': ''
                    }
            # 説明文を追加（• で始まる行）
            elif current_item and line.strip().startswith('•'):
                current_item['description'] += line.strip()[1:].strip() + '\n'

        # 最後のアイテムを追加
        if current_item:
            items.append(current_item)

        return items

    def _send_news_embed(self, item: Dict, index: int, webhook_url: str = None) -> bool:
        """
        個別のニュースをEmbed形式で送信

        Args:
            item: ニュース項目
            index: ニュース番号
            webhook_url: 送信先のWebhook URL

        Returns:
            送信成功したかどうか
        """
        # カテゴリ別の色分け
        category_colors = {
            '新型車': 0xFF0000,
            '新製品': 0xFF6600,
            'IT': 0x0066FF,
            'EV': 0x00FF00,
            '半導体': 0x9900FF,
            '技術革新': 0xFFD700,
            '製造技術': 0xFF1493,
            'AI': 0x00CED1,
            'ロボティクス': 0xFF4500,
            'スマートシティ': 0x32CD32,
        }

        color = category_colors.get(item['category'], 0x5865F2)  # デフォルトはDiscordの青

        embed = {
            "title": f"{index}. [{item['category']}] {item['title'][:200]}",
            "description": item['description'][:2000],
            "color": color,
            "footer": {
                "text": f"カテゴリ: {item['category']}"
            }
        }

        payload = {"embeds": [embed]}
        return self._send_webhook(payload, webhook_url)

    def _create_links_section(self, articles: List[Dict]) -> str:
        """
        記事リンクセクションを生成

        Args:
            articles: 記事のリスト

        Returns:
            記事リンクのテキスト
        """
        links = "## 📎 記事リンク\n\n"
        for i, article in enumerate(articles[:10], 1):
            links += f"{i}. [{article['title'][:80]}...]({article['url']})\n"
        return links
