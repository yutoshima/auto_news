---
title: "mobile_scanner で本の ISBN を読む。裏表紙の2段バーコードは両方 EAN-13 だった"
source: "Zenn"
category: "it"
published: 2026-10-14T02:00:21
url: https://zenn.dev/hk_work/articles/mobile-scanner-isbn-barcode
---

# mobile_scanner で本の ISBN を読む。裏表紙の2段バーコードは両方 EAN-13 だった

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 02:00
- **URL**: [https://zenn.dev/hk_work/articles/mobile-scanner-isbn-barcode](https://zenn.dev/hk_work/articles/mobile-scanner-isbn-barcode)

## 概要

蔵書管理アプリ「本棚（hondana）」を Flutter で個人開発しています。本の登録は、裏表紙のバーコードをカメラで読んで ISBN を取り、そこから書誌を引く流れです。書誌の引き方は openBD と Google Books で ISBN から書誌を引く に書きました。この記事はその手前、バーコードを読む部分の話です。
バーコードの読み取りには mobile_scanner 7.2.0 を使っています。

 カメラの権限
先に設定だけ書いておきます。iOS は Info.plist に用途の説明が要ります。無いとカメラを開いた時点でアプリが落ちます。
&lt;key&gt;NS...

---

*この記事は自動収集システムによって保存されました。*
