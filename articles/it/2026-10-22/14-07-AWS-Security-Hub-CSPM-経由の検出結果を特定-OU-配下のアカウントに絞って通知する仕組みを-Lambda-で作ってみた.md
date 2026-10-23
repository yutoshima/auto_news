---
title: "AWS Security Hub CSPM 経由の検出結果を特定 OU 配下のアカウントに絞って通知する仕組みを Lambda で作ってみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-22T14:07:52
url: https://dev.classmethod.jp/articles/security-hub-cspm-notify-specific-ou-lambda/
---

# AWS Security Hub CSPM 経由の検出結果を特定 OU 配下のアカウントに絞って通知する仕組みを Lambda で作ってみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 14:07
- **URL**: [https://dev.classmethod.jp/articles/security-hub-cspm-notify-specific-ou-lambda/](https://dev.classmethod.jp/articles/security-hub-cspm-notify-specific-ou-lambda/)

## 概要

Security Hub CSPM 経由の検出結果を特定 OU 配下のアカウントに絞って通知する仕組みを Lambda で実装してみました。AWS Organizations の API を活用して対象アカウントを動的に判定し、SNS 経由で通知します。

---

*この記事は自動収集システムによって保存されました。*
