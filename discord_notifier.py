import requests
from typing import List, Dict, Optional
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


class DiscordNotifier:
    """Discord Webhookを使ってニュースを配信するクラス"""

    def __init__(self):
        self.webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

        if not self.webhook_url:
            raise ValueError("DISCORD_WEBHOOK_URL が設定されていません")

        # 発表タイプ別の色分け
        self.color_scheme = {
            'Official_Debut': 0xFF0000,    # 赤 - 正式発表（最重要）
            'Facelift': 0xFF6600,          # オレンジ - マイナーチェンジ
            'Concept': 0x0066FF,           # 青 - コンセプトカー
            'Prototype': 0x9900FF,         # 紫 - プロトタイプ
            'Limited_Edition': 0xFFD700,   # 金 - 限定モデル
            'Unknown': 0x00FF00,           # 緑 - その他
        }

    def send_daily_summary(self, summary_text: str) -> bool:
        """
        日次ニュースサマリーを送信

        Args:
            summary_text: 要約されたニューステキスト

        Returns:
            送信成功したかどうか
        """
        # 2000文字制限対策
        if len(summary_text) > 2000:
            chunks = self._split_text(summary_text, 2000)
            for i, chunk in enumerate(chunks):
                success = self._send_message(chunk)
                if not success:
                    return False
            return True
        else:
            return self._send_message(summary_text)

    def send_new_car_alert(self, car_info: Dict) -> bool:
        """
        新型車情報をリッチな形式で送信

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

        return self._send_webhook(payload)

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

    def _send_message(self, content: str) -> bool:
        """シンプルなテキストメッセージを送信"""
        payload = {"content": content}
        return self._send_webhook(payload)

    def _send_webhook(self, payload: Dict) -> bool:
        """Webhookにペイロードを送信"""
        try:
            response = requests.post(self.webhook_url, json=payload)

            if response.status_code in [200, 204]:
                return True
            else:
                print(f"❌ Discord送信失敗: ステータスコード {response.status_code}")
                return False

        except Exception as e:
            print(f"❌ Discord送信エラー: {str(e)}")
            return False

    def _split_text(self, text: str, max_length: int) -> List[str]:
        """長いテキストを分割"""
        chunks = []
        current_chunk = ""

        for line in text.split('\n'):
            if len(current_chunk) + len(line) + 1 > max_length:
                chunks.append(current_chunk)
                current_chunk = line + '\n'
            else:
                current_chunk += line + '\n'

        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def test_connection(self) -> bool:
        """接続テスト"""
        return self._send_message("✅ Discord接続テストに成功しました！")
