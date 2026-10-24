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

    def fetch_readme(self, full_name: str, max_chars: int = 4000) -> str:
        """リポジトリのREADME本文を取得する（取得できなければ空文字）"""
        headers = {"Accept": "application/vnd.github.raw+json", "User-Agent": "auto_news"}
        token = os.getenv("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"Bearer {token}"
        try:
            response = requests.get(f"https://api.github.com/repos/{full_name}/readme", headers=headers, timeout=30)
            if response.status_code != 200:
                return ""
            # 画像やバッジのリンクは説明の役に立たないので落とす
            text = re.sub(r"!\[[^\]]*\]\([^)]*\)|<img[^>]*>", "", response.text)
            return text[:max_chars]
        except requests.RequestException:
            return ""


def explain_repository(analyzer, repo: Dict, readme: str) -> str:
    """
    リポジトリの説明文とREADMEから、何ができるのかを日本語で分かりやすく説明する

    Returns:
        日本語の説明（失敗時は説明文を翻訳しただけのもの）
    """
    prompt = f"""以下のGitHubリポジトリが「何をするものか」を、エンジニアでない人にも伝わるように日本語で説明してください。

条件:
- 2〜3文、全体で200文字以内
- 1文目で「何ができるものか」を一言で言う
- 2文目以降で、使い道や注目されている理由が分かれば書く
- 専門用語は必要なら短く言い換える
- 説明文のみを出力し、前置きや見出しは不要

リポジトリ: {repo['name']}
言語: {repo.get('language') or '不明'}
説明文: {repo.get('description') or 'なし'}

README（抜粋）:
{readme or 'なし'}"""

    # 評価用モデルで失敗・空回答だった場合は翻訳用モデルでもう一度試す
    models = [analyzer.scoring_model]
    if analyzer.model != analyzer.scoring_model:
        models.append(analyzer.model)

    for model in models:
        try:
            response = analyzer.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "あなたは技術の話を分かりやすく伝える日本語のテックライターです。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                # 回答前の思考でトークンを使い切って本文が空になることがあるため多めに取る
                max_tokens=4000
            )
            explanation = (response.choices[0].message.content or "").strip()
            if explanation:
                return explanation
            print(f"  ⚠️  説明が空でした ({repo['name']}, {model}, finish_reason={response.choices[0].finish_reason})")
        except Exception as e:
            print(f"  ⚠️  説明の生成エラー ({repo['name']}, {model}): {str(e)}")

    return analyzer.translate_to_japanese(repo.get('description', ''))


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
