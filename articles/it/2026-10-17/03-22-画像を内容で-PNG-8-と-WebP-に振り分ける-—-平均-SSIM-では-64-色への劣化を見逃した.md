---
title: "画像を内容で PNG-8 と WebP に振り分ける — 平均 SSIM では 64 色への劣化を見逃した"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-17T03:22:25
url: https://qiita.com/jhao29784/items/8af054655e77defc6163
---

# 画像を内容で PNG-8 と WebP に振り分ける — 平均 SSIM では 64 色への劣化を見逃した

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月17日 03:22
- **URL**: [https://qiita.com/jhao29784/items/8af054655e77defc6163](https://qiita.com/jhao29784/items/8af054655e77defc6163)

## 概要

業務のアップロード処理は、どの画像も同じ JPEG 設定で圧縮しています。商品写真はそれで困りません。困るのは運用担当が上げてくる注文画面や管理画面のスクリーンショットで、文字のまわりが灰色にざらつきます。そこで、スクショはパレット PNG、写真は WebP と、中身を見て...

---

*この記事は自動収集システムによって保存されました。*
