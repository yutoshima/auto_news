---
title: "Customer-managed runtimesでコールドスタートは速くなる?サイズの大きなライブラリをZIPにパッケージングする場合と比較してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-26T07:16:53
url: https://dev.classmethod.jp/articles/lambda-cmr-vs-zip-coldstart/
---

# Customer-managed runtimesでコールドスタートは速くなる?サイズの大きなライブラリをZIPにパッケージングする場合と比較してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月26日 07:16
- **URL**: [https://dev.classmethod.jp/articles/lambda-cmr-vs-zip-coldstart/](https://dev.classmethod.jp/articles/lambda-cmr-vs-zip-coldstart/)

## 概要

CMRに大きなライブラリを入れた場合と、AWS管理のランタイムでZIPに全て同梱した場合で、コールドスタートを比較しました。
平均値と中央値はCMRの方が優秀な結果が出ており、コンテナイメージ形式のLambdaと同様にチャンクを遅延ロードしているような雰囲気でした。

---

*この記事は自動収集システムによって保存されました。*
