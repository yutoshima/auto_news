---
title: "AWS SDK for JavaScript v3 で requestTimeout を設定したのに、時間切れにならない原因を教えてください"
source: "DevelopersIO"
category: "it"
published: 2026-10-25T01:00:10
url: https://dev.classmethod.jp/articles/tsnote-sdk-js-v3-requesttimeout-throwonrequesttimeout/
---

# AWS SDK for JavaScript v3 で requestTimeout を設定したのに、時間切れにならない原因を教えてください

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月25日 01:00
- **URL**: [https://dev.classmethod.jp/articles/tsnote-sdk-js-v3-requesttimeout-throwonrequesttimeout/](https://dev.classmethod.jp/articles/tsnote-sdk-js-v3-requesttimeout-throwonrequesttimeout/)

## 概要

AWS SDK for JavaScript v3 で `requestTimeout` を設定しても効かなくなった問題と、その解決方法を紹介します。@smithy/node-http-handler の仕様変更により `throwOnRequestTimeout: true` の設定が必要になりました。

---

*この記事は自動収集システムによって保存されました。*
