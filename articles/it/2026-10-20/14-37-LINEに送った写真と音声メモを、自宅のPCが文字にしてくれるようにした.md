---
title: "LINEに送った写真と音声メモを、自宅のPCが文字にしてくれるようにした"
source: "Zenn"
category: "it"
published: 2026-10-20T14:37:43
url: https://zenn.dev/hilopon/articles/line-local-ai-photo-voice-capture
---

# LINEに送った写真と音声メモを、自宅のPCが文字にしてくれるようにした

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月20日 14:37
- **URL**: [https://zenn.dev/hilopon/articles/line-local-ai-photo-voice-capture](https://zenn.dev/hilopon/articles/line-local-ai-photo-voice-capture)

## 概要

会議のホワイトボードを写真に撮る。帰り道に「来週までに見積り」と声で残す。ここまでは誰でもやっています。問題はそのあとで、撮った写真も録った声も、二度と開かない。私のスマホには、読み返されたことのない音声メモが何十本も眠っています。
そこで、LINEに写真か音声を送るだけで、自宅のPCが文字に起こして、日記用のリポジトリへ分類してしまってくれる仕組みを作りました。文字起こしも要約もクラウドのAIは使わず、全部手元のGPUでやっています。

 なぜクラウドに投げなかったのか
最初は当然、クラウドのAPIに投げるつもりでした。精度もいいし、作るのも楽です。ただ、これは毎日使う物です。日記の写...

---

*この記事は自動収集システムによって保存されました。*
