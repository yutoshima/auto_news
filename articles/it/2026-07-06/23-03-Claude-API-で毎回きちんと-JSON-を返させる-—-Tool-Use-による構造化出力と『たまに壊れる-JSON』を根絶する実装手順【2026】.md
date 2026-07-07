---
title: "Claude API で毎回きちんと JSON を返させる — Tool Use による構造化出力と『たまに壊れる JSON』を根絶する実装手順【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-07-06T23:03:47
url: https://qiita.com/yureki_lab/items/efa3caa0d009a8f6c35f
---

# Claude API で毎回きちんと JSON を返させる — Tool Use による構造化出力と『たまに壊れる JSON』を根絶する実装手順【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年07月06日 23:03
- **URL**: [https://qiita.com/yureki_lab/items/efa3caa0d009a8f6c35f](https://qiita.com/yureki_lab/items/efa3caa0d009a8f6c35f)

## 概要

Claude に「JSON で返して」とプロンプトで頼むと、9割はうまくいくのに、たまに前置きの文章が混ざったり末尾が切れたりして json.loads が落ちる。本番のバッチでこれをやられると地味に痛い。この記事は、その「たまに壊れる」を Tool Use（関数呼び出し）...

---

*この記事は自動収集システムによって保存されました。*
