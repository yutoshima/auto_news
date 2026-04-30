---
title: "宣言的スキーマ管理ツール pistachio を作成しました"
source: "Zenn"
category: "it"
published: 2026-04-30T03:52:05
url: https://zenn.dev/kanmu_dev/articles/16789ef1f4283a
---

# 宣言的スキーマ管理ツール pistachio を作成しました

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月30日 03:52
- **URL**: [https://zenn.dev/kanmu_dev/articles/16789ef1f4283a](https://zenn.dev/kanmu_dev/articles/16789ef1f4283a)

## 概要

プラットフォームチームの菅原です。
最近、pistachioという宣言的スキーマ管理ツールを作成し[1]、本番環境のDBマイグレーションに導入したので紹介させてください。

 pistachioについて
https://github.com/winebarrel/pistachio
「宣言的スキーマ管理」はTerraformのように「あるべきスキーマの状態」を記述し、差分を埋めるDDLを実行することでDBマイグレーションを行う方法です。
同様のツールとしてはatlasやsqldef、拙作ですがRidgepole、最近のものだとpgschemaなどがあります。
pistachioはPost...

---

*この記事は自動収集システムによって保存されました。*
