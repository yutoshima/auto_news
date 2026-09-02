---
title: "会話セッションを邪魔せずに Claude Code / Codex / Cursor を外部イベントで動かすCLIの作り方まとめ"
source: "Zenn"
category: "it"
published: 2026-09-01T01:03:04
url: https://zenn.dev/coji/articles/artifactshare-preview-claude-codex-cursor
---

# 会話セッションを邪魔せずに Claude Code / Codex / Cursor を外部イベントで動かすCLIの作り方まとめ

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月01日 01:03
- **URL**: [https://zenn.dev/coji/articles/artifactshare-preview-claude-codex-cursor](https://zenn.dev/coji/articles/artifactshare-preview-claude-codex-cursor)

## 概要

これはなに？
今年の5月ごろから、Artifact Share というサービスを自分で使うためにソース公開で作り続けています。AIエージェントが作ったHTMLやMarkdownをURLで共有するものです。そのCLIに preview というローカルコマンドを追加しました。ブラウザ上でファイルの要素をクリックして指摘を書くと、Claude Code・Codex・Cursor がファイルを直し、ブラウザが自動リロードで結果を見せます。動画が一番早いです。

ここから先は仕組みの話です。サインイン・アップロード不要のローカル機能で、実装は公開しています。
https://github.co...

---

*この記事は自動収集システムによって保存されました。*
