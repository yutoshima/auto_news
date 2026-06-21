---
title: "基数変換ツールを作る — BigInt で桁数無制限、そして「小数の循環」を検出する"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-06-20T23:44:15
url: https://qiita.com/sen-ltd/items/29f3ec2ab515ac184eef
---

# 基数変換ツールを作る — BigInt で桁数無制限、そして「小数の循環」を検出する

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年06月20日 23:44
- **URL**: [https://qiita.com/sen-ltd/items/29f3ec2ab515ac184eef](https://qiita.com/sen-ltd/items/29f3ec2ab515ac184eef)

## 概要

2〜36 進数を相互変換するツールを作った。「parseInt(s, 16) でいいのでは？」と思うかもしれないが、まともに作ると 2 つの落とし穴がある: (1) Number は 2^53 を超えると精度が壊れるので大きい数は BigInt が要る、(2) 小数部は、...

---

*この記事は自動収集システムによって保存されました。*
