---
title: "オントロジーで AI に業務知識を渡す — AWS の OSS「Context Ontology Accelerator」を試してみた"
source: "Zenn"
category: "it"
published: 2026-08-03T05:26:48
url: https://zenn.dev/aws_japan/articles/context-ontology-accelerator-deploy
---

# オントロジーで AI に業務知識を渡す — AWS の OSS「Context Ontology Accelerator」を試してみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月03日 05:26
- **URL**: [https://zenn.dev/aws_japan/articles/context-ontology-accelerator-deploy](https://zenn.dev/aws_japan/articles/context-ontology-accelerator-deploy)

## 概要

はじめに
こんにちは、AWS Japan でソリューションアーキテクトをしているいなりくです。
AI エージェントを業務に入れようとすると、必ず同じ壁にぶつかります。データはあるのに、業務の意味が渡っていないという壁です。

「売上」は total_amount の合計なのか、送料込みなのか、キャンセル分を引くのか
「この注文はキャンセルできる？」に答えるには、注文テーブルの状態とキャンセルポリシー文書の両方が必要
「アクティブ顧客」の定義は部署ごとに違うかもしれない

これらは人間の頭と社内ドキュメントの中にあり、information_schema には存在しません。LLM がい...

---

*この記事は自動収集システムによって保存されました。*
