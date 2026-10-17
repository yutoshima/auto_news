---
title: "ユニバースが679銘柄に膨張してToo many open filesで落ちた話 — Noneの扱いひとつで上限が崩れる"
source: "Qiita (Python)"
category: "it"
published: 2026-10-16T23:59:41
url: https://qiita.com/sakutto-panda/items/22974731bb563fdd070b
---

# ユニバースが679銘柄に膨張してToo many open filesで落ちた話 — Noneの扱いひとつで上限が崩れる

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月16日 23:59
- **URL**: [https://qiita.com/sakutto-panda/items/22974731bb563fdd070b](https://qiita.com/sakutto-panda/items/22974731bb563fdd070b)

## 概要

3行まとめ

RakuScan（自分用の投資分析ツール）で月次のユニバース（スクリーニング対象銘柄群）再構築後、日次バッチがToo many open filesで落ちた
原因をたどると、本来200銘柄前後のはずのユニバースが679銘柄まで膨張していた。フィルタの「データ...

---

*この記事は自動収集システムによって保存されました。*
