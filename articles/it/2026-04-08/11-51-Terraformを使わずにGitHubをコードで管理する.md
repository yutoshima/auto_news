---
title: "Terraformを使わずにGitHubをコードで管理する"
source: "Zenn"
category: "it"
published: 2026-04-08T11:51:11
url: https://zenn.dev/babarot/articles/github-as-code-with-gh-infra
---

# Terraformを使わずにGitHubをコードで管理する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月08日 11:51
- **URL**: [https://zenn.dev/babarot/articles/github-as-code-with-gh-infra](https://zenn.dev/babarot/articles/github-as-code-with-gh-infra)

## 概要

GitHubのリポジトリをどう管理するか
GitHubのリポジトリが増えてくると、設定の管理が地味に厄介になります。OSSを複数持っていると、merge strategyやRuleset、Actionsの許可設定など、毎回似たような設定をしていくことになります。また、新しい設定を入れていくときも古いリポジトリでは漏れがちで、久しぶりに開いたら古い設定だった、みたいなこともよくあります。
例えば、Goで新しいCLIツールを書いて公開するとします。visibilityをpublicにして、squash mergeだけ有効にして、auto delete head branchesをオンにす...

---

*この記事は自動収集システムによって保存されました。*
