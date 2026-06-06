---
title: "ffmpeg.wasmで動画→GIF変換をブラウザ完結。COOP/COEPヘッダなしで動かすcore選択の話"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-06-05T22:53:29
url: https://qiita.com/sakutto-panda/items/f8775c663a1415fe621b
---

# ffmpeg.wasmで動画→GIF変換をブラウザ完結。COOP/COEPヘッダなしで動かすcore選択の話

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年06月05日 22:53
- **URL**: [https://qiita.com/sakutto-panda/items/f8775c663a1415fe621b](https://qiita.com/sakutto-panda/items/f8775c663a1415fe621b)

## 概要

3行まとめ

ffmpeg.wasm で動画→GIF 変換をブラウザだけで完結させた（サーバー送信なし）
マルチスレッド core は SharedArrayBuffer を要求し、COOP/COEP ヘッダが必須になる。静的ホスティングでこれを避けるためシングルスレッド...

---

*この記事は自動収集システムによって保存されました。*
