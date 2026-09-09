---
title: "Herdr × git worktree × Claude Codeの相性がいい話"
source: "Zenn"
category: "it"
published: 2026-09-08T06:20:57
url: https://zenn.dev/gemcook/articles/herdr-worktree-parallel
---

# Herdr × git worktree × Claude Codeの相性がいい話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月08日 06:20
- **URL**: [https://zenn.dev/gemcook/articles/herdr-worktree-parallel](https://zenn.dev/gemcook/articles/herdr-worktree-parallel)

## 概要

こんにちは、村中（@wage790）です。関西でバックエンド・クラウドインフラのエンジニアをしています。
普段の開発でClaude Codeを1つだけ動かしていると、その応答をただ待つ時間ができてしまいます。そこで、Claude Codeを複数並べて動かすことにしました。ただそれだと、同じ作業ディレクトリで2つ動かした場合に、片方がgit switchするともう片方が読んでいるファイルまで入れ替わってしまいます。それを避けるため、git worktreeで作業ディレクトリを分けました。
ただ、worktreeを作るたびにgit worktree addを打ってディレクトリを移動するのが今...

---

*この記事は自動収集システムによって保存されました。*
