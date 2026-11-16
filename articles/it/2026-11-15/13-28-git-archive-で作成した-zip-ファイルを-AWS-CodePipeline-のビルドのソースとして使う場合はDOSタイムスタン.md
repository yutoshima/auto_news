---
title: "git archive で作成した zip ファイルを AWS CodePipeline のビルドのソースとして使う場合はDOSタイムスタン"
source: "はてブ テクノロジー"
category: "it"
published: 2026-11-15T13:28:59
url: https://zenn.dev/yskszk63/articles/codepipeline-zip-dostime
---

# git archive で作成した zip ファイルを AWS CodePipeline のビルドのソースとして使う場合はDOSタイムスタン

## メタデータ

- **情報源**: はてブ テクノロジー
- **カテゴリ**: it
- **公開日時**: 2026年11月15日 13:28
- **URL**: [https://zenn.dev/yskszk63/articles/codepipeline-zip-dostime](https://zenn.dev/yskszk63/articles/codepipeline-zip-dostime)

## 概要

git archive で作成した zip ファイルを AWS CodePipeline のビルドのソースとして使う場合はDOSタイムスタンプをUTCで作成すべき 要約 zip ファイルには DOS タイムスタンプと拡張タイムスタンプがある DOS タイムスタンプはタイムゾーン無しのタイムスタンプ 拡張タイムスタンプはUTCで格納されたタイムスタンプ AWS C...

---

*この記事は自動収集システムによって保存されました。*
