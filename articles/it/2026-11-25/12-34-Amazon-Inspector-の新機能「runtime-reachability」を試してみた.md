---
title: "Amazon Inspector の新機能「runtime reachability」を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-25T12:34:02
url: https://dev.classmethod.jp/articles/inspector-runtime-reachability-ecr-ec2/
---

# Amazon Inspector の新機能「runtime reachability」を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月25日 12:34
- **URL**: [https://dev.classmethod.jp/articles/inspector-runtime-reachability-ecr-ec2/](https://dev.classmethod.jp/articles/inspector-runtime-reachability-ecr-ec2/)

## 概要

脆弱なパッケージを ECR イメージと EC2 インスタンスに仕込み、finding の runtime reachability を見ました。WORKDIR の内側のパッケージと、起動した httpd の httpd-core が REACHABLE に、WORKDIR の外側のパッケージと nginx、PHP が NOT_REACHABLE になりました。

---

*この記事は自動収集システムによって保存されました。*
