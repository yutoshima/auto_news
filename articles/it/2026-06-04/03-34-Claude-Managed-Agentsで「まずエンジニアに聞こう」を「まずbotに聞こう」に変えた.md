---
title: "Claude Managed Agentsで「まずエンジニアに聞こう」を「まずbotに聞こう」に変えた"
source: "Zenn"
category: "it"
published: 2026-06-04T03:34:04
url: https://zenn.dev/dinii/articles/d7be3acc43d868
---

# Claude Managed Agentsで「まずエンジニアに聞こう」を「まずbotに聞こう」に変えた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月04日 03:34
- **URL**: [https://zenn.dev/dinii/articles/d7be3acc43d868](https://zenn.dev/dinii/articles/d7be3acc43d868)

## 概要

はじめに
ダイニーでは、開発チーム宛ての質問（社内では dev-help と呼んでいます）が日に8件ほど来ます。1件 10 分でも、積み上がれば月に数十時間が消えていきます。前回の記事では、過去の dev-help チケットを RAG（過去の文書を意味検索で引っ張ってくる仕組み）で引いて関連事例をスレッドに貼る bot を作り、リードタイム中央値を 10 日から 5 時間まで縮めました。
ただし、構造上どうしても拾えない層が残っていました。「いまのデータ・ログ・コードを、人が読みに行かないと答えが出ない」 タイプの問い合わせです。
今回作った @ask-anything は、この層を...

---

*この記事は自動収集システムによって保存されました。*
