---
title: "JavaScriptの非同期処理はepollで成り立っているのか、Node.js、Deno、Bunそれぞれで覗いてみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-17T14:55:39
url: https://dev.classmethod.jp/articles/hasuto-js-async-epoll-node-deno-bun/
---

# JavaScriptの非同期処理はepollで成り立っているのか、Node.js、Deno、Bunそれぞれで覗いてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月17日 14:55
- **URL**: [https://dev.classmethod.jp/articles/hasuto-js-async-epoll-node-deno-bun/](https://dev.classmethod.jp/articles/hasuto-js-async-epoll-node-deno-bun/)

## 概要

Node.js、Deno、Bunをstraceし、非同期処理がLinuxのepollで待っているかを比べました。ネットワークの応答は3つともepollで待つ一方、Promiseとawaitのしくみ自体はOSを使わず、ファイルは別スレッドが読み込んでいました。fetch()がOSに届くタイミングの違いも紹介します。

---

*この記事は自動収集システムによって保存されました。*
