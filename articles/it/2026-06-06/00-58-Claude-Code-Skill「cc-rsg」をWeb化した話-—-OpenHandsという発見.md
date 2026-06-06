---
title: "Claude Code Skill「cc-rsg」をWeb化した話 — OpenHandsという発見"
source: "Zenn"
category: "it"
published: 2026-06-06T00:58:41
url: https://zenn.dev/daishiro/articles/openhands-cc-rsg-webapp
---

# Claude Code Skill「cc-rsg」をWeb化した話 — OpenHandsという発見

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月06日 00:58
- **URL**: [https://zenn.dev/daishiro/articles/openhands-cc-rsg-webapp](https://zenn.dev/daishiro/articles/openhands-cc-rsg-webapp)

## 概要

はじめに
こんにちは、daishir0です。
普段はClaude Codeを趣味や開発でガシガシ使っていて、副産物として小さなSkillをいくつか作って公開しています。GitHubはこちらです。
今回の記事は、自作のClaude Code Skillである cc-rsg（リバース仕様書ジェネレータ）を、Webアプリケーションとして提供できる形に作り直した経緯の話です。OpenHandsという基盤を使ったらこれが想像以上にハマって、ついでに「これって自分のAgentic AI基盤の作り方そのものが変わるな…」と気づいた、というところまでを書きます。
実装の細かい話と、最後に所感を少しだ...

---

*この記事は自動収集システムによって保存されました。*
