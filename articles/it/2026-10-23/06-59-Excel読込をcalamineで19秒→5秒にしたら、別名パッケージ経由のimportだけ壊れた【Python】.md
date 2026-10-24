---
title: "Excel読込をcalamineで19秒→5秒にしたら、別名パッケージ経由のimportだけ壊れた【Python】"
source: "Zenn"
category: "it"
published: 2026-10-23T06:59:26
url: https://zenn.dev/cutlet_of_pork/articles/calamine-excel-read-alias-package-import
---

# Excel読込をcalamineで19秒→5秒にしたら、別名パッケージ経由のimportだけ壊れた【Python】

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月23日 06:59
- **URL**: [https://zenn.dev/cutlet_of_pork/articles/calamine-excel-read-alias-package-import](https://zenn.dev/cutlet_of_pork/articles/calamine-excel-read-alias-package-import)

## 概要

import=FAIL ModuleNotFoundError No module named 'src.core'
sys_path_changed True
AI に任せた実装の受け入れ検査で、この 2 行が出た。実装した側の報告では、テストは 204 件全部通っていた。

 何をしていたか
社内の生産管理システムから落とした進捗一覧の Excel を、pandas で読んで絞り込むスクリプトがある。22,267 行 × 88 列。この read_excel が 20 秒前後かかっていて、一括実行だと同じファイルを 2 回読むので 40 秒近く待たされる。
少し前に、Excel の読...

---

*この記事は自動収集システムによって保存されました。*
