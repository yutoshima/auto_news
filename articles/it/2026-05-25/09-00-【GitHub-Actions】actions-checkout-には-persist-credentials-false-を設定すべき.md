---
title: "【GitHub Actions】actions/checkout には persist-credentials: false を設定すべき"
source: "Zenn"
category: "it"
published: 2026-05-25T09:00:07
url: https://zenn.dev/kou_pg_0131/articles/gha-checkout-persist-credentials
---

# 【GitHub Actions】actions/checkout には persist-credentials: false を設定すべき

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月25日 09:00
- **URL**: [https://zenn.dev/kou_pg_0131/articles/gha-checkout-persist-credentials](https://zenn.dev/kou_pg_0131/articles/gha-checkout-persist-credentials)

## 概要

結論
actions/checkout アクションを使用する際は、persist-credentials: false を設定するべきです。
- uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
  with:
    # ↓これ
    persist-credentials: false # デフォルトは true

なぜか？
後続のステップからファイル経由であっさり GitHub トークンを抜き取れてしまうため。

---

*この記事は自動収集システムによって保存されました。*
