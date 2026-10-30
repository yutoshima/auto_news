---
title: "縦動画の字幕に合わせて VOICEVOX の声を置き、区間を声の長さに伸ばして、BGM を下げつつ -16 LUFS にそろえる（Python＋ffmpeg）"
source: "Qiita (Python)"
category: "it"
published: 2026-10-30T01:53:43
url: https://qiita.com/MisaNeco/items/796bf1563612417457c0
---

# 縦動画の字幕に合わせて VOICEVOX の声を置き、区間を声の長さに伸ばして、BGM を下げつつ -16 LUFS にそろえる（Python＋ffmpeg）

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年10月30日 01:53
- **URL**: [https://qiita.com/MisaNeco/items/796bf1563612417457c0](https://qiita.com/MisaNeco/items/796bf1563612417457c0)

## 概要

字幕つきの縦動画（1080×1920・30fps、30秒前後）を何本も作っています。映像は台本の JSON から書き出す仕組みがすでにあるので、そこに読み上げ音声と BGM を足す make_voice.py（340行ほど）を書きました。
難しかったのは、声の長さが字幕の表...

---

*この記事は自動収集システムによって保存されました。*
