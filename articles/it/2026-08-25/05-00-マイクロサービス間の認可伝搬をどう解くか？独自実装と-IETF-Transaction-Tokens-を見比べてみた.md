---
title: "マイクロサービス間の認可伝搬をどう解くか？独自実装と IETF Transaction Tokens を見比べてみた"
source: "Zenn"
category: "it"
published: 2026-08-25T05:00:05
url: https://zenn.dev/layerx/articles/e01465a15e79c2
---

# マイクロサービス間の認可伝搬をどう解くか？独自実装と IETF Transaction Tokens を見比べてみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月25日 05:00
- **URL**: [https://zenn.dev/layerx/articles/e01465a15e79c2](https://zenn.dev/layerx/articles/e01465a15e79c2)

## 概要

こんにちは。アカウント基盤開発部でエンジニアをしている tkmt (たくまつ) です。
今回は、IETF で標準化が進んでいる Transaction Tokens について調査してまとめてみました。というのも、この Transaction Tokens が解こうとしている課題が、バクラクが抱えていた課題とほとんど同じだったためです。
実はバクラクでは、同じ課題を解くための仕組みを自作しています。バクラクで実装された仕組みは、ドラフトで検討されている内容とどこが同じで、どこが違うのか読み比べてみたく調査しました。

 解きたかった課題
バクラクには、プロダクトを跨いで認可を行いたいケース...

---

*この記事は自動収集システムによって保存されました。*
