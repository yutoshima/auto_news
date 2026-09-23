---
title: "Claude API の stop_reason を全パターン処理する実装手順 — max_tokens で切れても HTTP 200・stop_details は refusal のときだけ・pause_turn の再開、3つのハマりどころ【2026】"
source: "Qiita (Python)"
category: "it"
published: 2026-09-22T23:02:43
url: https://qiita.com/yureki_lab/items/09f6ed07a52c78b1363b
---

# Claude API の stop_reason を全パターン処理する実装手順 — max_tokens で切れても HTTP 200・stop_details は refusal のときだけ・pause_turn の再開、3つのハマりどころ【2026】

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月22日 23:02
- **URL**: [https://qiita.com/yureki_lab/items/09f6ed07a52c78b1363b](https://qiita.com/yureki_lab/items/09f6ed07a52c78b1363b)

## 概要

はじめに / 対象と前提
Claude API を叩いて返ってきたレスポンスから、いきなり response.content[0].text を読んでいないだろうか。自分はやっていた。そして本番で JSON パースがランダムに落ちた。
原因は stop_reason を見...

---

*この記事は自動収集システムによって保存されました。*
