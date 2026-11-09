---
title: "自宅サーバーにClaude Codeを常駐させ、スマホから24時間指示を出す（Remote Control＋systemd）"
source: "Zenn"
category: "it"
published: 2026-11-08T08:59:05
url: https://zenn.dev/samurai_works/articles/114a5e654ca295
---

# 自宅サーバーにClaude Codeを常駐させ、スマホから24時間指示を出す（Remote Control＋systemd）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月08日 08:59
- **URL**: [https://zenn.dev/samurai_works/articles/114a5e654ca295](https://zenn.dev/samurai_works/articles/114a5e654ca295)

## 概要

自宅の Linux サーバーに Claude Code を入れて常駐させ、外出先のスマホから「サーバー上の実ファイルを触る作業」を頼めるようにしました。ポート開放なし・VPN なしで動く構成です。
実際にセットアップしてハマったところも含めて、手順をまとめます。
!
2026年11月時点の情報です。Claude Code は更新が速いので、画面や挙動が変わっている可能性があります。最新の公式ドキュメントもあわせて確認してください。
筆者は Anthropic とは無関係の一ユーザーです。設定は自己責任でお願いします。


 この記事でできるようになること

自宅サーバーで Claude ...

---

*この記事は自動収集システムによって保存されました。*
