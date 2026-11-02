---
title: "GitHub Actions で checkout@v7 のようなバージョン指定を書くのはやめよう！ 時代は actions.lock！"
source: "Zenn"
category: "it"
published: 2026-10-29T03:48:15
url: https://zenn.dev/progate/articles/24b1140180300c
---

# GitHub Actions で checkout@v7 のようなバージョン指定を書くのはやめよう！ 時代は actions.lock！

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月29日 03:48
- **URL**: [https://zenn.dev/progate/articles/24b1140180300c](https://zenn.dev/progate/articles/24b1140180300c)

## 概要

Progate で業務委託エンジニアをしている横江( @yokoe24 )です！
セキュリティの話が重要視される昨今ですが、
みなさんは GitHub Actions の Workflow ファイルで、こんな書き方をしていませんか？
steps:
  - uses: actions/checkout@v7
・・・私は書いています！！🙈
この記事を書きながら、過去の個人リポジトリ、直さなきゃなぁ……って思っています。

 @v7 と書くリスク
npm の件などで敏感になっている方はお気付きかもしれませんが、
@v7 のような書き方は、最新の v7.x.x に追従でき便利な一方[1]、
攻撃...

---

*この記事は自動収集システムによって保存されました。*
