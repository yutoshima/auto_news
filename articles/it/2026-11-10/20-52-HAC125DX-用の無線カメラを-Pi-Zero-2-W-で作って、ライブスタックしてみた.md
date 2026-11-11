---
title: "HAC125DX 用の無線カメラを Pi Zero 2 W で作って、ライブスタックしてみた"
source: "Zenn"
category: "it"
published: 2026-11-10T20:52:00
url: https://zenn.dev/tsukitsukiss/articles/livestack-hac125dx-wireless-camera
---

# HAC125DX 用の無線カメラを Pi Zero 2 W で作って、ライブスタックしてみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 20:52
- **URL**: [https://zenn.dev/tsukitsukiss/articles/livestack-hac125dx-wireless-camera](https://zenn.dev/tsukitsukiss/articles/livestack-hac125dx-wireless-camera)

## 概要

はじめに
撮影専用の天体望遠鏡である Sky-Watcher の HAC125DX（口径 125mm、焦点距離 250mm、F2）のプライムフォーカスに載せる 無線カメラ を作りました。Raspberry Pi Zero 2 W に IMX585 というイメージセンサを取り付け、バッテリーで動かし、撮った RAW を Wi-Fi で PC に送って、PC 側でライブスタックします。
この記事では、なぜ無線にしたのか、筐体の光路長をどう追い込んだのか、実際に使ってどこでつまずいたのかを書きます。
!
IMX585 基板（SE585MBD-C）は、SOHO エンタープライズ様から提供を受...

---

*この記事は自動収集システムによって保存されました。*
