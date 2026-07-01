---
title: "UNIXタイムスタンプ変換でハマるタイムゾーンの罠——datetime-localはローカル解釈、表示はIntlに任せる"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-06-30T23:00:38
url: https://qiita.com/sakutto-panda/items/34febfbd8ede86d0e628
---

# UNIXタイムスタンプ変換でハマるタイムゾーンの罠——datetime-localはローカル解釈、表示はIntlに任せる

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年06月30日 23:00
- **URL**: [https://qiita.com/sakutto-panda/items/34febfbd8ede86d0e628](https://qiita.com/sakutto-panda/items/34febfbd8ede86d0e628)

## 概要

UNIXタイムスタンプ ⇔ 日時の変換ツールは「new Date(ts * 1000) して toLocaleString() するだけ」に見える。だが実際に作ると、タイムゾーンの扱いで静かにバグる。特に「日時 → タイムスタンプ」方向で、

---

*この記事は自動収集システムによって保存されました。*
