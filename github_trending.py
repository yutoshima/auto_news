import json
import os
import re
import requests
from datetime import datetime
from typing import List, Dict, Set
from bs4 import BeautifulSoup


class GitHubTrendingCollector:
    """GitHub Trendingから「今日増えたスター数」の多いリポジトリを取得するクラス"""

    TRENDING_URL = "https://github.com/trending"

    def fetch_repositories(self, since: str = "daily") -> List[Dict]:
        """
        Trendingページを取得し、期間内に増えたスター数の多い順に返す

        Args:
            since: 'daily', 'weekly', 'monthly'

        Returns:
            リポジトリ情報のリスト（stars_gained の多い順）
        """
        response = requests.get(
            self.TRENDING_URL,
            params={"since": since},
            headers={"User-Agent": "Mozilla/5.0 (auto_news)"},
            timeout=30,
        )
        response.raise_for_status()

        repos = self._parse(response.text)
        # Trendingページは独自の順位で並んでいるので、増えたスター数で並べ直す
        repos.sort(key=lambda r: r["stars_gained"], reverse=True)
        return repos

    def _parse(self, html: str) -> List[Dict]:
        """TrendingページのHTMLからリポジトリ情報を抜き出す"""
        soup = BeautifulSoup(html, "html.parser")
        repos = []

        for row in soup.select("article.Box-row"):
            link = row.select_one("h2 a")
            if not link or not link.get("href"):
                continue
            full_name = link["href"].strip("/")

            description_tag = row.select_one("p")
            language_tag = row.select_one('[itemprop="programmingLanguage"]')
            stars_tag = row.select_one('a[href$="/stargazers"]')

            stars_gained = 0
            for span in row.select("span"):
                match = re.search(r"([\d,]+)\s+stars?\s+(today|this week|this month)", span.get_text())
                if match:
                    stars_gained = self._to_int(match.group(1))
                    break

            repos.append({
                "name": full_name,
                "url": f"https://github.com/{full_name}",
                "description": description_tag.get_text(strip=True) if description_tag else "",
                "language": language_tag.get_text(strip=True) if language_tag else "",
                "stars": self._to_int(stars_tag.get_text()) if stars_tag else 0,
                "stars_gained": stars_gained,
            })

        return repos

    def _to_int(self, text: str) -> int:
        digits = re.sub(r"[^\d]", "", text)
        return int(digits) if digits else 0


class TrendingHistory:
    """過去にTrendingに載ったリポジトリを記録するクラス（articles/ 配下に保存してコミットする）"""

    def __init__(self, path: str = "articles/github_trending_history.json"):
        self.path = path
        self.history: Dict[str, Dict] = {}
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                self.history = json.load(f)

    def known_names(self) -> Set[str]:
        return set(self.history)

    def record(self, repos: List[Dict]) -> None:
        """今回見たリポジトリを履歴に追加して保存する"""
        today = datetime.now().strftime("%Y-%m-%d")
        for repo in repos:
            entry = self.history.setdefault(repo["name"], {"first_seen": today})
            entry["last_seen"] = today

        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2, sort_keys=True)
