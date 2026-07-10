---
title: "Cloudflareだけで独自ドメインメールをGmailから送受信できるようになってた"
source: "Zenn"
category: "it"
published: 2026-07-10T02:33:47
url: https://zenn.dev/9m/articles/d08dcc093e1bbf
---

# Cloudflareだけで独自ドメインメールをGmailから送受信できるようになってた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月10日 02:33
- **URL**: [https://zenn.dev/9m/articles/d08dcc093e1bbf](https://zenn.dev/9m/articles/d08dcc093e1bbf)

## 概要

TL;DR

メールの受信は Cloudflare Email Routing
メールの送信は Cloudflare Email Sending
メールの閲覧・作成には普段使っているGmailを利用

CloudflareがSMTPをしゃべれるようになったので、Gmailのエイリアスに追加できるぞ！

 独自ドメインのメールアドレスにお金かけたくない問題
個人開発をやっているとポコポコ独自ドメインが増えていきますが、メールの送受信は頭が痛い問題です(費用面で)。Google Workspaceを契約するのが一番理想なのですが、ドメインごとに毎月800円も払っていられません。
そのため...

---

*この記事は自動収集システムによって保存されました。*
