---
title: "JaCoCoはどうやってカバレッジを測っているのか"
source: "Zenn"
category: "it"
published: 2026-11-10T08:41:07
url: https://zenn.dev/chikina/articles/jacoco-coverage-bytecode
---

# JaCoCoはどうやってカバレッジを測っているのか

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 08:41
- **URL**: [https://zenn.dev/chikina/articles/jacoco-coverage-bytecode](https://zenn.dev/chikina/articles/jacoco-coverage-bytecode)

## 概要

Eclipseでカバレッジを計測すると、コードが赤、黄、緑で色分けされます。
どこまでカバーできたかは見えるものの、その色をどう決めているかは見えづらく、ちょっと黒魔術っぽく感じます。
Eclipseからカバレッジを計測し、結果を表示するプラグインがEclEmmaで、計測と解析にはJaCoCoを使います。
その仕組みを調べるため、計測前後のclassファイルを比べてみました。
小さなJUnitのテストで、計測用の命令が実行されてから、記録を解析してソースに色が付くまでを追います。
後半では本体とテストを分けた例も使い、同じ計測方式で分岐や途中終了の表示を説明します。
classファイル自...

---

*この記事は自動収集システムによって保存されました。*
