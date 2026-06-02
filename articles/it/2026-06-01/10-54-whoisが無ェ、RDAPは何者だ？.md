---
title: "whoisが無ェ、RDAPは何者だ？"
source: "Zenn"
category: "it"
published: 2026-06-01T10:54:30
url: https://zenn.dev/digeon/articles/fb563703bcfc96
---

# whoisが無ェ、RDAPは何者だ？

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月01日 10:54
- **URL**: [https://zenn.dev/digeon/articles/fb563703bcfc96](https://zenn.dev/digeon/articles/fb563703bcfc96)

## 概要

Who is RDAP?
30秒でわかるかもしれない概要

社内システムが使っているドメインが少し気になったのでwhoisをかけてみたが引っかからずにgetaddrinfoで落ちた
調べてみると2025年1月28日にgTLDのWHOIS提供義務は公式に消滅していた
現在は後継のRDAP（HTTPS + JSON）がgTLD登録データの正式な配信手段になっている
ただしccTLD（.jp等）は別の時間軸で動いていて、.jpの権威RDAPは存在しない
にもかかわらず、自社管理 .jp ドメインなら国内レジストラのRDAPでも引けてしまう（stealth RDAP）
40年余り使われたwh...

---

*この記事は自動収集システムによって保存されました。*
