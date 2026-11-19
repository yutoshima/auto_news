---
title: "nginx2root の HTTP/2 脆弱性2件を AWS 構成ごとに整理してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-18T19:08:09
url: https://dev.classmethod.jp/articles/nginx-http2-rce-aws-mitigation/
---

# nginx2root の HTTP/2 脆弱性2件を AWS 構成ごとに整理してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月18日 19:08
- **URL**: [https://dev.classmethod.jp/articles/nginx-http2-rce-aws-mitigation/](https://dev.classmethod.jp/articles/nginx-http2-rce-aws-mitigation/)

## 概要

NGINX の HTTP/2 の脆弱性 CVE-2026-123007・CVE-2026-123633 の仕組みと AWS 構成ごとの影響を整理し、修正版を使えない環境の緩和策として、http2 off で curl --http2 の接続が HTTP/1.1 になることを Docker で確認しました。

---

*この記事は自動収集システムによって保存されました。*
