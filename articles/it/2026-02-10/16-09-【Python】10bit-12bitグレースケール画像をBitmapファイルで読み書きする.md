---
title: "【Python】10bit/12bitグレースケール画像をBitmapファイルで読み書きする"
source: "Qiita (Python)"
category: "it"
published: 2026-02-10T16:09:55
url: https://qiita.com/ImagingSolAkira/items/bab80298e1323830d52a
---

# 【Python】10bit/12bitグレースケール画像をBitmapファイルで読み書きする

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年02月10日 16:09
- **URL**: [https://qiita.com/ImagingSolAkira/items/bab80298e1323830d52a](https://qiita.com/ImagingSolAkira/items/bab80298e1323830d52a)

## 概要

はじめに
産業用カメラや医療画像の分野では、8bit (0～255) では階調が不足するため、10bit (0～1023) や12bit (0～4095) のグレースケール画像が使われます。
しかし、OpenCVの cv2.imread() / cv2.imwrite()...

---

*この記事は自動収集システムによって保存されました。*
