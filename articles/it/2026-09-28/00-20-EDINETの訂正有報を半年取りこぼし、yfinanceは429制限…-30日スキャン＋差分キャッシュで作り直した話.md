---
title: "EDINETの訂正有報を半年取りこぼし、yfinanceは429制限… 30日スキャン＋差分キャッシュで作り直した話"
source: "Qiita (Python)"
category: "it"
published: 2026-09-28T00:20:36
url: https://qiita.com/akkyey/items/12a8df355ee895ed73d4
---

# EDINETの訂正有報を半年取りこぼし、yfinanceは429制限… 30日スキャン＋差分キャッシュで作り直した話

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月28日 00:20
- **URL**: [https://qiita.com/akkyey/items/12a8df355ee895ed73d4](https://qiita.com/akkyey/items/12a8df355ee895ed73d4)

## 概要

TL;DR

東証の約3,900社を毎朝取り込むパイプラインで、訂正有報の取りこぼしと yfinance の429エラー（レート制限）に悩まされていました。
毎朝過去30日分の書類一覧（メタデータ）だけをスキャンし、取得済みの書類は再ダウンロードしないようにしました。財務...

---

*この記事は自動収集システムによって保存されました。*
