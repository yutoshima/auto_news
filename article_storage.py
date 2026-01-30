import os
from typing import List, Dict
from datetime import datetime
import re


class ArticleStorage:
    """記事をMarkdown形式でGitHubに保存するクラス"""

    def __init__(self, base_dir: str = "articles"):
        """
        初期化

        Args:
            base_dir: 記事を保存するベースディレクトリ
        """
        self.base_dir = base_dir
        self._ensure_directory_exists(self.base_dir)

    def save_articles(self, articles: List[Dict]) -> int:
        """
        記事をMarkdown形式で保存

        Args:
            articles: 記事のリスト

        Returns:
            保存した記事数
        """
        saved_count = 0

        for article in articles:
            try:
                self.save_article(article)
                saved_count += 1
            except Exception as e:
                print(f"⚠️  記事の保存に失敗: {article['title'][:50]} - {str(e)}")

        print(f"✅ {saved_count}/{len(articles)} 件の記事を保存しました")
        return saved_count

    def save_article(self, article: Dict) -> str:
        """
        単一の記事をMarkdownファイルとして保存

        Args:
            article: 記事の辞書

        Returns:
            保存したファイルパス
        """
        # 公開日時からディレクトリとファイル名を生成
        published = datetime.fromisoformat(article['published'])
        date_dir = published.strftime('%Y-%m-%d')
        time_prefix = published.strftime('%H-%M')

        # カテゴリ別のディレクトリ
        category = article.get('category', 'other')
        category_dir = os.path.join(self.base_dir, category, date_dir)
        self._ensure_directory_exists(category_dir)

        # ファイル名生成（タイトルをサニタイズ）
        safe_title = self._sanitize_filename(article['title'])
        filename = f"{time_prefix}-{safe_title}.md"
        filepath = os.path.join(category_dir, filename)

        # Markdown内容を生成
        markdown_content = self._generate_markdown(article)

        # ファイルに保存
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        return filepath

    def _generate_markdown(self, article: Dict) -> str:
        """
        記事からMarkdown形式のコンテンツを生成

        Args:
            article: 記事の辞書

        Returns:
            Markdownフォーマットの文字列
        """
        published = datetime.fromisoformat(article['published'])

        # フロントマター（メタデータ）
        frontmatter = f"""---
title: "{article['title']}"
source: "{article['source']}"
category: "{article.get('category', 'other')}"
published: {article['published']}
url: {article['url']}
---

# {article['title']}

## メタデータ

- **情報源**: {article['source']}
- **カテゴリ**: {article.get('category', 'other')}
- **公開日時**: {published.strftime('%Y年%m月%d日 %H:%M')}
- **URL**: [{article['url']}]({article['url']})

## 概要

{article['summary']}

---

*この記事は自動収集システムによって保存されました。*
"""

        return frontmatter

    def _sanitize_filename(self, title: str, max_length: int = 80) -> str:
        """
        タイトルからファイル名として安全な文字列を生成

        Args:
            title: 記事タイトル
            max_length: 最大文字数

        Returns:
            サニタイズされた文字列
        """
        # 使用できない文字を置換
        safe_title = re.sub(r'[\\/:*?"<>|]', '-', title)

        # スペースをハイフンに
        safe_title = safe_title.replace(' ', '-')

        # 連続するハイフンを1つに
        safe_title = re.sub(r'-+', '-', safe_title)

        # 前後のハイフンを削除
        safe_title = safe_title.strip('-')

        # 長さ制限
        if len(safe_title) > max_length:
            safe_title = safe_title[:max_length].rstrip('-')

        return safe_title

    def _ensure_directory_exists(self, directory: str):
        """
        ディレクトリが存在しない場合は作成

        Args:
            directory: ディレクトリパス
        """
        if not os.path.exists(directory):
            os.makedirs(directory)

    def get_storage_stats(self) -> Dict:
        """
        保存された記事の統計情報を取得

        Returns:
            統計情報の辞書
        """
        stats = {
            'total': 0,
            'by_category': {},
            'by_date': {}
        }

        if not os.path.exists(self.base_dir):
            return stats

        # カテゴリごとの統計
        for category in os.listdir(self.base_dir):
            category_path = os.path.join(self.base_dir, category)
            if not os.path.isdir(category_path):
                continue

            count = 0
            for date_dir in os.listdir(category_path):
                date_path = os.path.join(category_path, date_dir)
                if os.path.isdir(date_path):
                    files = [f for f in os.listdir(date_path) if f.endswith('.md')]
                    count += len(files)

                    # 日付ごとの統計
                    if date_dir not in stats['by_date']:
                        stats['by_date'][date_dir] = 0
                    stats['by_date'][date_dir] += len(files)

            stats['by_category'][category] = count
            stats['total'] += count

        return stats
