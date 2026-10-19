---
title: "【ネットワークセキュリティ入門】VLANとACLだけで安全？管理プレーンの分離とマイクロセグメンテーションを整理してみた - Qiita"
source: "はてブ テクノロジー"
category: "it"
published: 2026-10-18T01:59:23
url: https://qiita.com/maromaro_nw/items/2a191e16f1b32235886d
---

# 【ネットワークセキュリティ入門】VLANとACLだけで安全？管理プレーンの分離とマイクロセグメンテーションを整理してみた - Qiita

## メタデータ

- **情報源**: はてブ テクノロジー
- **カテゴリ**: it
- **公開日時**: 2026年10月18日 01:59
- **URL**: [https://qiita.com/maromaro_nw/items/2a191e16f1b32235886d](https://qiita.com/maromaro_nw/items/2a191e16f1b32235886d)

## 概要

VLANごとにレイヤー2のネットワークは分離されますが、L3スイッチでVLAN間ルーティングを有効にすると、異なるVLAN間でも通信できるようになります。 そこでACL（Access Control List）を設定し、営業部から経理部への通信は拒否、営業部から業務サーバーへのHTTPS通信は許可、といった制御を行います。 通信経路とACLの...

---

*この記事は自動収集システムによって保存されました。*
