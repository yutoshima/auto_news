---
title: "脱CDKしてTerraformに移行すべきn個の理由(または私はなぜCDKをやめたか)"
source: "Zenn"
category: "it"
published: 2026-04-05T01:00:07
url: https://zenn.dev/okazu_dm/articles/d35f863365cabf
---

# 脱CDKしてTerraformに移行すべきn個の理由(または私はなぜCDKをやめたか)

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月05日 01:00
- **URL**: [https://zenn.dev/okazu_dm/articles/d35f863365cabf](https://zenn.dev/okazu_dm/articles/d35f863365cabf)

## 概要

こんにちは。常日頃からCDKに対してのアツい気持ちを抱いているSREの@okazu_dmです。
今回はCDKをやめてTerraformを使いましょう、という記事のタイトルですが、具体的には以下のような話をします。

CDKとTerraformの性質の違い
CDKで運用すると辛い点
とはいえTerraformでも辛いケースはある
移行判断の軸

ツール自体の比較よりは、運用のときに起きる困りごとや運用時に考えることの話をします。

 おことわり
そもそもこの記事自体が大いにポジショントークなので、偏りがあることはご了承ください。
それはそれとして、記事の誤りのご指摘やCDKのメリットについ...

---

*この記事は自動収集システムによって保存されました。*
