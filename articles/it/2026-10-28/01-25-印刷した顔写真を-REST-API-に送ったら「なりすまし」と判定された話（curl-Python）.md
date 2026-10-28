---
title: "印刷した顔写真を REST API に送ったら「なりすまし」と判定された話（curl / Python）"
source: "Qiita (Python)"
category: "it"
published: 2026-10-28T01:25:41
url: https://qiita.com/ToshikazuOhno/items/e50c18845ed7748ac5e7
---

# 印刷した顔写真を REST API に送ったら「なりすまし」と判定された話（curl / Python）

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 01:25
- **URL**: [https://qiita.com/ToshikazuOhno/items/e50c18845ed7748ac5e7](https://qiita.com/ToshikazuOhno/items/e50c18845ed7748ac5e7)

## 概要

顔認証は「登録された本人か」を見る仕組みで、カメラの前にあるのが本物の顔か、写真や画面かは見ていません。そのため、本人の写真をかざすだけで通ってしまうことがあります。
これを防ぐのが「なりすまし判定（ライブネス検知）」です。本記事では、画像1枚を POST するだけで判定で...

---

*この記事は自動収集システムによって保存されました。*
