---
title: "歌詞の読み誤りを音源で補正する（CTC forced alignmentの尤度で読み候補を選ぶ）"
source: "Qiita (Python)"
category: "it"
published: 2026-07-21T22:36:02
url: https://qiita.com/shimajiroxyz/items/684dc6e2b132ee82e1bb
---

# 歌詞の読み誤りを音源で補正する（CTC forced alignmentの尤度で読み候補を選ぶ）

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年07月21日 22:36
- **URL**: [https://qiita.com/shimajiroxyz/items/684dc6e2b132ee82e1bb](https://qiita.com/shimajiroxyz/items/684dc6e2b132ee82e1bb)

## 概要

概要
歌詞テキストをカナ読みに変換して歌唱音源に forced alignment するパイプラインで、読み推定の誤り（例:「二人」→ニニン）によりアライメントが行ごと崩壊する問題に当たりました。対策として、読みエンジン間で読みが割れた行だけ、CTCの対数尤度（force...

---

*この記事は自動収集システムによって保存されました。*
