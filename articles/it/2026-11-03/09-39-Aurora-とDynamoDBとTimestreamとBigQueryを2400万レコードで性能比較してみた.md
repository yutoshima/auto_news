---
title: "Aurora とDynamoDBとTimestreamとBigQueryを2400万レコードで性能比較してみた"
source: "Zenn"
category: "it"
published: 2026-11-03T09:39:55
url: https://zenn.dev/ncdc/articles/c47df2c1f32e0c
---

# Aurora とDynamoDBとTimestreamとBigQueryを2400万レコードで性能比較してみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 09:39
- **URL**: [https://zenn.dev/ncdc/articles/c47df2c1f32e0c](https://zenn.dev/ncdc/articles/c47df2c1f32e0c)

## 概要

はじめに
私が働いているNCDCでは、年に1回会社でハッカソンをやっています。
興味ある技術を使って、なんか作るみたいなイベントです。
私はDBに最近興味を持っているので、DBの性能を比較するWEBアプリを構築しました。
そこで得た知見をこの記事に残したいと思います。
この記事は、ベンチマーク記事というより、性能を比較しようとして気づいたことをまとめたものです。
フェアな比較の難しさも、あわせて書いています。
数値は、私が組んだ条件での参考値として読んでください。

 シナリオ
電車の IoT センサーが、1 秒に 1 回、5 つの値を記録して、データが溜まっていく場面を想定しました...

---

*この記事は自動収集システムによって保存されました。*
