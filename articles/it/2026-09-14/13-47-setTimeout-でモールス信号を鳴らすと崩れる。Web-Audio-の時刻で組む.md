---
title: "setTimeout でモールス信号を鳴らすと崩れる。Web Audio の時刻で組む"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-09-14T13:47:35
url: https://qiita.com/hashito/items/3387a000ac3883becfc7
---

# setTimeout でモールス信号を鳴らすと崩れる。Web Audio の時刻で組む

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年09月14日 13:47
- **URL**: [https://qiita.com/hashito/items/3387a000ac3883becfc7](https://qiita.com/hashito/items/3387a000ac3883becfc7)

## 概要

背景
モールス信号の変換ツールを作っていました。
文字と符号を入れ替えるだけなら対応表を引くだけで終わる話で、正直そこは何も面白くない…
詰まったのは音のほうです。
モールスは「音の長さと間隔そのもの」が情報なので、リズムが崩れると別の文字に聞こえてしまう。
最初 set...

---

*この記事は自動収集システムによって保存されました。*
