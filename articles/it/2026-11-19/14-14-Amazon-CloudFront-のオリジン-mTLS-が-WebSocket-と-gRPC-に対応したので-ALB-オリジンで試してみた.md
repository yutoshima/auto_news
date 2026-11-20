---
title: "Amazon CloudFront のオリジン mTLS が WebSocket と gRPC に対応したので ALB オリジンで試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T14:14:47
url: https://dev.classmethod.jp/articles/amazon-cloudfront-origin-mtls-websocket-grpc/
---

# Amazon CloudFront のオリジン mTLS が WebSocket と gRPC に対応したので ALB オリジンで試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 14:14
- **URL**: [https://dev.classmethod.jp/articles/amazon-cloudfront-origin-mtls-websocket-grpc/](https://dev.classmethod.jp/articles/amazon-cloudfront-origin-mtls-websocket-grpc/)

## 概要

ALB をオリジンにして、WebSocket と gRPC でも CloudFront の Origin mTLS を使えるか試しました。1つのクライアント証明書で、HTTP、WebSocket、gRPC のどれも ALB の mTLS（verify）を通りました。

---

*この記事は自動収集システムによって保存されました。*
