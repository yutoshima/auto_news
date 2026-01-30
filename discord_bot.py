#!/usr/bin/env python3
"""
Discord Bot - 質問応答機能
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import openai
import json
from datetime import datetime
from pathlib import Path

load_dotenv()


class NewsBot(commands.Bot):
    """車とITニュース配信Bot"""

    def __init__(self):
        # Bot設定
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        super().__init__(command_prefix="!", intents=intents)

        # Gemini-3-flash用のクライアント設定
        self.llm_client = openai.OpenAI(
            api_key=os.getenv("POE_API_KEY"),
            base_url="https://api.poe.com/v1",
        )
        self.conversation_model = "gemini-3-flash"

        print(f"🤖 会話モデル: {self.conversation_model}")

    async def on_ready(self):
        """Bot起動時の処理"""
        print(f"✅ Botがログインしました: {self.user.name} (ID: {self.user.id})")
        print(f"🔗 招待URL: https://discord.com/api/oauth2/authorize?client_id={self.user.id}&permissions=2048&scope=bot")
        print("=" * 60)

    async def on_message(self, message):
        """メッセージ受信時の処理"""
        # 自分自身のメッセージは無視
        if message.author == self.user:
            return

        # メンションされた場合のみ応答
        if self.user.mentioned_in(message):
            await self.handle_question(message)

        # コマンドも処理
        await self.process_commands(message)

    async def handle_question(self, message):
        """質問に答える"""
        # メンションを除去して質問内容を取得
        question = message.content.replace(f'<@{self.user.id}>', '').strip()

        if not question:
            await message.channel.send("何か質問してください！")
            return

        # タイピングインジケーターを表示
        async with message.channel.typing():
            # 最近の記事データを読み込み
            recent_articles = self.load_recent_articles()

            # コンテキストを作成
            context = self.create_context(recent_articles)

            # LLMで回答を生成
            try:
                response_text = await self.generate_response(question, context)

                # Discord文字数制限対応（2000文字）
                if len(response_text) > 2000:
                    # 複数メッセージに分割
                    chunks = self.split_message(response_text, 2000)
                    for chunk in chunks:
                        await message.channel.send(chunk)
                else:
                    await message.channel.send(response_text)

            except Exception as e:
                print(f"❌ エラー: {str(e)}")
                await message.channel.send(f"⚠️ エラーが発生しました: {str(e)}")

    def load_recent_articles(self):
        """最近保存された記事を読み込む"""
        articles = []
        articles_dir = Path("articles")

        if not articles_dir.exists():
            return articles

        # 最新の日付ディレクトリを取得
        for category in ["it", "car"]:
            category_dir = articles_dir / category
            if not category_dir.exists():
                continue

            # 日付ディレクトリを取得してソート
            date_dirs = sorted([d for d in category_dir.iterdir() if d.is_dir()], reverse=True)

            # 最新2日分の記事を読み込み
            for date_dir in date_dirs[:2]:
                for md_file in date_dir.glob("*.md"):
                    try:
                        with open(md_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            # フロントマターから情報を抽出
                            if content.startswith('---'):
                                parts = content.split('---', 2)
                                if len(parts) >= 3:
                                    article_info = self.parse_frontmatter(parts[1])
                                    articles.append(article_info)
                    except Exception as e:
                        continue

        return articles[:30]  # 最新30件まで

    def parse_frontmatter(self, frontmatter_text):
        """フロントマターをパース"""
        info = {}
        for line in frontmatter_text.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                info[key.strip()] = value.strip().strip('"')
        return info

    def create_context(self, articles):
        """記事データからコンテキストを作成"""
        if not articles:
            return "現在、参照可能な記事データはありません。"

        context = "以下は最近収集したニュース記事のリストです:\n\n"
        for i, article in enumerate(articles[:20], 1):
            context += f"{i}. {article.get('title', '不明')}\n"
            context += f"   カテゴリ: {article.get('category', '不明')}\n"
            context += f"   ソース: {article.get('source', '不明')}\n"
            if article.get('url'):
                context += f"   URL: {article['url']}\n"
            context += "\n"

        return context

    async def generate_response(self, question, context):
        """LLMで回答を生成"""
        system_prompt = """あなたは車とIT業界に詳しい専門アシスタントです。
ユーザーからの質問に対して、提供されたニュース記事の情報を参考にしながら、正確で分かりやすい回答を提供してください。

回答のガイドライン:
- 簡潔で分かりやすく答える
- 記事の情報を参照する場合は、出典を明記する
- 不明な点は正直に「情報がありません」と答える
- 専門用語は適度に説明を加える
- 絵文字を適度に使って親しみやすく
"""

        user_prompt = f"""【最近のニュース記事】
{context}

【ユーザーの質問】
{question}

上記の記事情報を参考にして、質問に答えてください。"""

        response = self.llm_client.chat.completions.create(
            model=self.conversation_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        return response.choices[0].message.content

    def split_message(self, text, max_length=2000):
        """長いメッセージを分割"""
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


def main():
    """メイン処理"""
    bot_token = os.getenv("DISCORD_BOT_TOKEN")

    if not bot_token:
        print("❌ DISCORD_BOT_TOKEN が設定されていません")
        print("環境変数を設定してください")
        return

    bot = NewsBot()

    @bot.command(name="help")
    async def help_command(ctx):
        """ヘルプメッセージ"""
        help_text = """
**🤖 車とITニュースBot - 使い方**

**質問の仕方:**
@ボット名 質問内容

**例:**
@ボット名 今日のITニュースは？
@ボット名 最近の新型車情報を教えて
@ボット名 AIに関する記事はある？

**その他:**
`!help` - このヘルプを表示
"""
        await ctx.send(help_text)

    @bot.command(name="status")
    async def status_command(ctx):
        """Bot状態確認"""
        # 記事数をカウント
        articles = bot.load_recent_articles()
        await ctx.send(f"✅ Bot稼働中\n📰 参照可能な記事: {len(articles)}件")

    # Botを起動
    print("🚀 Botを起動しています...")
    print("終了するには Ctrl+C を押してください")
    print("=" * 60)

    try:
        bot.run(bot_token)
    except KeyboardInterrupt:
        print("\n👋 Botを終了します")
    except Exception as e:
        print(f"❌ エラーが発生しました: {str(e)}")


if __name__ == "__main__":
    main()
