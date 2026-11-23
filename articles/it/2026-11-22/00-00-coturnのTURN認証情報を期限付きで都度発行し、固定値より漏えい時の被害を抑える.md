---
title: "coturnのTURN認証情報を期限付きで都度発行し、固定値より漏えい時の被害を抑える"
source: "Qiita トレンド"
category: "it"
published: 2026-11-22T00:00:12
url: https://qiita.com/takumi_engineer/items/50c27c11ccf08db3165a?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items
---

# coturnのTURN認証情報を期限付きで都度発行し、固定値より漏えい時の被害を抑える

## メタデータ

- **情報源**: Qiita トレンド
- **カテゴリ**: it
- **公開日時**: 2026年11月22日 00:00
- **URL**: [https://qiita.com/takumi_engineer/items/50c27c11ccf08db3165a?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items](https://qiita.com/takumi_engineer/items/50c27c11ccf08db3165a?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

## 概要

WebRTC配信でTURNサーバーに固定のユーザー名とパスワードを書くと、フロントのコードから抜かれて第三者の中継に使われるおそれがあります。この記事では、coturnの共有シークレット方式で、期限付きの認証情報をAPIから都度発行する方法を、動くコードで示します。

前提...

---

*この記事は自動収集システムによって保存されました。*
