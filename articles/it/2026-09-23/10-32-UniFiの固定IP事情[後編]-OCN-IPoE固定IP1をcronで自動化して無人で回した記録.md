---
title: "UniFiの固定IP事情[後編] OCN IPoE固定IP1をcronで自動化して無人で回した記録"
source: "Zenn"
category: "it"
published: 2026-09-23T10:32:51
url: https://zenn.dev/nwsejp/articles/unifi-japan-static-ip-operations
---

# UniFiの固定IP事情[後編] OCN IPoE固定IP1をcronで自動化して無人で回した記録

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月23日 10:32
- **URL**: [https://zenn.dev/nwsejp/articles/unifi-japan-static-ip-operations](https://zenn.dev/nwsejp/articles/unifi-japan-static-ip-operations)

## 概要

前編「UniFiの固定IP事情[前編] 使う方法と選び方まとめ」では、公開されている回避策を 5 系統に整理して選び方まで書いた。本稿はその続きで、選んだあとに何が起きるかを扱う。
系統1（OCN の IPoE 固定IPで hostname を注入する）を機器内の cron で自動化し、無人で回して測った記録だ。回避策そのものは系統1に限った内容だが、何が回避策を壊すのか（3 章）は、ゲートウェイの上で番人（常駐の書き戻し。本稿ではこう呼ぶ）を走らせる方式に共通する話になる。
本稿の要点は以下の 4 点だ。


再起動からの復旧には、WAN の DNS で IPv6 側の手動設定が必要。...

---

*この記事は自動収集システムによって保存されました。*
