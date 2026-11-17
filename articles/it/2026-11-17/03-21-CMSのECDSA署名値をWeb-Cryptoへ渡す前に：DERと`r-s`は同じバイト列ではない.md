---
title: "CMSのECDSA署名値をWeb Cryptoへ渡す前に：DERと`r || s`は同じバイト列ではない"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-11-17T03:21:30
url: https://qiita.com/heftykoo/items/513dec4462e594135816
---

# CMSのECDSA署名値をWeb Cryptoへ渡す前に：DERと`r || s`は同じバイト列ではない

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年11月17日 03:21
- **URL**: [https://qiita.com/heftykoo/items/513dec4462e594135816](https://qiita.com/heftykoo/items/513dec4462e594135816)

## 概要

CMS（Cryptographic Message Syntax）の署名を解析し、公開鍵と署名対象データを取り出してブラウザーのWeb Crypto APIで検証しようとしたとき、アルゴリズム名がどちらもECDSAであるにもかかわらず検証が通らないことがあります。原因の一つ...

---

*この記事は自動収集システムによって保存されました。*
