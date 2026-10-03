---
title: "Amazon Aurora DSQLは部分インデックスをサポートします"
source: "AWS What's New"
category: "it"
published: 2026-10-02T17:30:00
url: https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-dsql-partial-indexes/
---

# Amazon Aurora DSQLは部分インデックスをサポートします

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年10月02日 17:30
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-dsql-partial-indexes/](https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-dsql-partial-indexes/)

## 概要

<p><a href="https://aws.amazon.com/rds/aurora/dsql/">Amazon Aurora DSQL</a>は、テーブル全体の全行ではなく、条件を満たす行だけを格納する特定の部分集合上にインデックスを構築することを可能にしました。これにより、クエリのパフォーマンスが向上し、インデックスのストレージコストが削減されます。</p>
<p>多くのテーブルには、完了済みの長い履歴の中に、比較的小さな作業セットが共存しています。例えば、何年分もの履歴の中の「オープン注文」などです。CREATE INDEXにWHERE句を追加して、その作業セットだけをインデックス化します。インデックスは作業セットの分だけ小さなまま維持されます。</p>

---

*この記事は自動収集システムによって保存されました。*
