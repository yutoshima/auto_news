---
title: "画像をJPEG/PNG/WebPに変換する — Canvas toBlobの品質引数と、透過を白で潰す理由"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-30T23:57:38
url: https://qiita.com/sakutto-panda/items/3392f4f6bdbab0a28c16
---

# 画像をJPEG/PNG/WebPに変換する — Canvas toBlobの品質引数と、透過を白で潰す理由

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月30日 23:57
- **URL**: [https://qiita.com/sakutto-panda/items/3392f4f6bdbab0a28c16](https://qiita.com/sakutto-panda/items/3392f4f6bdbab0a28c16)

## 概要

3行まとめ

画像を JPEG・PNG・WebP に相互変換するブラウザ完結ツールを作った。中身は「 でデコード → Canvasに描画 → toBlob で再エンコード」の3手

toBlob の第3引数（品質 0〜1）はJPEG・WebPのような非可逆形式に...

---

*この記事は自動収集システムによって保存されました。*
