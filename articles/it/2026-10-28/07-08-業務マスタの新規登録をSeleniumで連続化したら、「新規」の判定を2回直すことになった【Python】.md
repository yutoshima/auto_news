---
title: "業務マスタの新規登録をSeleniumで連続化したら、「新規」の判定を2回直すことになった【Python】"
source: "Zenn"
category: "it"
published: 2026-10-28T07:08:48
url: https://zenn.dev/cutlet_of_pork/articles/selenium-rpa-new-entry-key-definition
---

# 業務マスタの新規登録をSeleniumで連続化したら、「新規」の判定を2回直すことになった【Python】

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 07:08
- **URL**: [https://zenn.dev/cutlet_of_pork/articles/selenium-rpa-new-entry-key-definition](https://zenn.dev/cutlet_of_pork/articles/selenium-rpa-new-entry-key-definition)

## 概要

同じキーの行が 1 件あります。新規の対象は、その行が無いものだけです。
登録し終わったデータを、わざともう一度流したときに出た行（語は少し伏せた）。「登録」は押さずに止まっている。
この 1 行が出るようになるまでに、何を「新規」と呼ぶかを 2 回直した。その後、同じキーの行があったときの扱いを分け、保留にしていた更新も入れて、今はこの 1 行はもう出ない。この記事はその順に書く。

 何をしていたか
社内の業務システムに、期間付きの値を持つマスタがある。1 行は、種別と組織と相手先と対象のコードと期間と値でできている。依頼が Excel で届くと、それを 1 件ずつ画面に打ち込む。
...

---

*この記事は自動収集システムによって保存されました。*
