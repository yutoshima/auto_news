---
title: "Amazon Aurora DSQL で大陸をまたぐマルチリージョンクラスター（東京とバージニア）を作成してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-20T09:36:40
url: https://dev.classmethod.jp/articles/aws-aurora-dsql-intercontinental-multi-region/
---

# Amazon Aurora DSQL で大陸をまたぐマルチリージョンクラスター（東京とバージニア）を作成してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月20日 09:36
- **URL**: [https://dev.classmethod.jp/articles/aws-aurora-dsql-intercontinental-multi-region/](https://dev.classmethod.jp/articles/aws-aurora-dsql-intercontinental-multi-region/)

## 概要

別大陸にある東京とバージニア北部をピア、オレゴンを witness として、Amazon Aurora DSQL のマルチリージョンクラスターを作成しました。ピアリングから2分以内に両クラスターが ACTIVE になり、どちらのエンドポイントで書き込んだ行も、もう一方の Region の SELECT で読み取れることを確認しました。

---

*この記事は自動収集システムによって保存されました。*
