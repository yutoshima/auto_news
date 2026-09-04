---
title: "Pythonのメール送信でSMTPをやめてHTTP APIに移行した話"
source: "Qiita (Python)"
category: "it"
published: 2026-09-04T00:05:05
url: https://qiita.com/iqbalabd/items/ab9023a80d50c919af03
---

# Pythonのメール送信でSMTPをやめてHTTP APIに移行した話

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月04日 00:05
- **URL**: [https://qiita.com/iqbalabd/items/ab9023a80d50c919af03](https://qiita.com/iqbalabd/items/ab9023a80d50c919af03)

## 概要

独自ドメインのメール送信をPythonで自動化している場合、99%のチュートリアルは smtplib を使う。標準ライブラリだし、メンテナンス不要だし、動く。
しかし、本番で使い続けると、SMTPの「動く」には条件が付くことがわかる。VPC内のLambdaからポート587が...

---

*この記事は自動収集システムによって保存されました。*
