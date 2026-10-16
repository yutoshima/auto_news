---
title: "Lambda Web Functions の実行環境を調べてみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-15T22:25:35
url: https://dev.classmethod.jp/articles/lambda-web-functions-runtime-environment/
---

# Lambda Web Functions の実行環境を調べてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 22:25
- **URL**: [https://dev.classmethod.jp/articles/lambda-web-functions-runtime-environment/](https://dev.classmethod.jp/articles/lambda-web-functions-runtime-environment/)

## 概要

AWS Lambda Web Functions の実行環境を調べました。CPU は Graviton3 世代の 2 vCPU で、OpenSSL の性能は c7g.large 相当でした。従来の Lambda、Lambda MicroVMs、EC2 と比較し、CPU 使用率が低いほど費用面で有利になる試算結果も紹介します。

---

*この記事は自動収集システムによって保存されました。*
