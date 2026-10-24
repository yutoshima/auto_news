---
title: "Expressのボット対策をローカルで検証する：monitorの404とenforceの403"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-24T02:29:19
url: https://qiita.com/webdecoy/items/5510dc54cb762c3b33fa
---

# Expressのボット対策をローカルで検証する：monitorの404とenforceの403

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月24日 02:29
- **URL**: [https://qiita.com/webdecoy/items/5510dc54cb762c3b33fa](https://qiita.com/webdecoy/items/5510dc54cb762c3b33fa)

## 概要

HTTP 404が返っても、ボット対策のミドルウェアがリクエストを止めたとは限りません。監視モードでは、拒否すべきという判定が付いていても、その後のルートが実行されます。
この記事では、通常のパスと自分で用意したデコイ用パスを比較し、判定結果・HTTPステータス・ルートの実...

---

*この記事は自動収集システムによって保存されました。*
