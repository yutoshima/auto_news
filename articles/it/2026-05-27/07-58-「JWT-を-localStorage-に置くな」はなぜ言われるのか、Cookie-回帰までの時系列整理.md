---
title: "「JWT を localStorage に置くな」はなぜ言われるのか、Cookie 回帰までの時系列整理"
source: "Zenn"
category: "it"
published: 2026-05-27T07:58:44
url: https://zenn.dev/khale/articles/web-session-jwt-cookie-history
---

# 「JWT を localStorage に置くな」はなぜ言われるのか、Cookie 回帰までの時系列整理

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月27日 07:58
- **URL**: [https://zenn.dev/khale/articles/web-session-jwt-cookie-history](https://zenn.dev/khale/articles/web-session-jwt-cookie-history)

## 概要

はじめに
Webセキュリティの第一人者である徳丸浩氏が X で、JWT と Cookie セッションの関係についてこんな投稿をされていました。

これはウェブAPI呼び出しの歴史から考えると腑に落ちるのですが、CORSの機能にCookie付与があることからもわかるように、

(1) 昔はクロスオリジンのAPIをCookieによるセッション管理で呼び出す方法が用いられていましたが、
(2) サードパーティクッキー規制などでそれが難しくなり、Authorizationヘッダによるトークン（保存先はlocalStorage）に変わるものの、
(3) 各APIの生トークンをクライアントに保持...

---

*この記事は自動収集システムによって保存されました。*
