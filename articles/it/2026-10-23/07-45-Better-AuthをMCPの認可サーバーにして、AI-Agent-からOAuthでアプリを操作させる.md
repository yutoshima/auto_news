---
title: "Better AuthをMCPの認可サーバーにして、AI Agent からOAuthでアプリを操作させる"
source: "Zenn"
category: "it"
published: 2026-10-23T07:45:06
url: https://zenn.dev/sakagi/articles/8caa896e649005
---

# Better AuthをMCPの認可サーバーにして、AI Agent からOAuthでアプリを操作させる

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月23日 07:45
- **URL**: [https://zenn.dev/sakagi/articles/8caa896e649005](https://zenn.dev/sakagi/articles/8caa896e649005)

## 概要

はじめに
WebアプリにMCPサーバーを追加し、Claudeから利用者本人としてデータを読み書きできるようにしました。アプリのログインは Microsoft Entra ID の SSO を使用し、AIに渡すトークンはBetter Authの@better-auth/mcpでアプリ自身が発行します。
プラグインを入れるだけで、認可サーバーに要るエンドポイントはひととおり揃います。
ただ、既定のままでは困る点がいくつかありました。
この記事では、認可の流れを追ったうえで、Better Authの設定と、実装のときに足した規則を紹介します。

 構成
Entra IDは利用者の認証だけを...

---

*この記事は自動収集システムによって保存されました。*
