---
title: "Amazon Linux 2023 の公式 SRPM から PHP 8.2.35 を CodeBuild でビルドしてみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-22T02:06:22
url: https://dev.classmethod.jp/articles/al2023-php-srpm-rebuild-codebuild/
---

# Amazon Linux 2023 の公式 SRPM から PHP 8.2.35 を CodeBuild でビルドしてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 02:06
- **URL**: [https://dev.classmethod.jp/articles/al2023-php-srpm-rebuild-codebuild/](https://dev.classmethod.jp/articles/al2023-php-srpm-rebuild-codebuild/)

## 概要

PHP の重大な脆弱性に対し、公式パッチが出るまでの間、AL2023 公式の SRPM をベースにソースだけを差し替えて修正版 RPM を自作する手順を紹介します。CodeBuild を使ったビルドからサーバーへの適用まで、実際に試した方法をまとめました。

---

*この記事は自動収集システムによって保存されました。*
