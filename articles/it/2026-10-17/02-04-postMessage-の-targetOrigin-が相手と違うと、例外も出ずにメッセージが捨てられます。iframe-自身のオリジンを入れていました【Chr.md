---
title: "postMessage の targetOrigin が相手と違うと、例外も出ずにメッセージが捨てられます。iframe 自身のオリジンを入れていました【Chromium 141 で実測】"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-17T02:04:22
url: https://qiita.com/Rapls/items/9c6f8ef8edbb7343486b
---

# postMessage の targetOrigin が相手と違うと、例外も出ずにメッセージが捨てられます。iframe 自身のオリジンを入れていました【Chromium 141 で実測】

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月17日 02:04
- **URL**: [https://qiita.com/Rapls/items/9c6f8ef8edbb7343486b](https://qiita.com/Rapls/items/9c6f8ef8edbb7343486b)

## 概要

iframe の中から parent.postMessage(msg, targetOrigin) を呼ぶとき、targetOrigin が親ページのオリジンと違うと、メッセージは捨てられます。例外は投げられず、postMessage() は普通に戻ってきます。残るのは、開...

---

*この記事は自動収集システムによって保存されました。*
