---
title: "git archive で作成した zip ファイルを AWS CodePipeline のビルドのソースとして使う場合はDOSタイムスタン"
source: "Zenn"
category: "it"
published: 2026-10-25T02:37:59
url: https://zenn.dev/yskszk63/articles/codepipeline-zip-dostime
---

# git archive で作成した zip ファイルを AWS CodePipeline のビルドのソースとして使う場合はDOSタイムスタン

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月25日 02:37
- **URL**: [https://zenn.dev/yskszk63/articles/codepipeline-zip-dostime](https://zenn.dev/yskszk63/articles/codepipeline-zip-dostime)

## 概要

git archive で作成した zip ファイルを AWS CodePipeline のビルドのソースとして使う場合はDOSタイムスタンプをUTCで作成すべき

 要約

zip ファイルには DOS タイムスタンプと拡張タイムスタンプがある
DOS タイムスタンプはタイムゾーン無しのタイムスタンプ
拡張タイムスタンプはUTCで格納されたタイムスタンプ
AWS CodePipeline は zip ファイル展開時にDOSタイムスタンプでmtimeを設定するようだ
AWS CodePipeline のソースとして利用する zip ファイルは TZ=UTC として作成すべき


 何...

---

*この記事は自動収集システムによって保存されました。*
