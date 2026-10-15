---
title: "開発しながら同じPCでローカルLLMを動かしてみた話"
source: "Zenn"
category: "it"
published: 2026-10-14T01:31:20
url: https://zenn.dev/sumasate_tec/articles/test-local-llm
---

# 開発しながら同じPCでローカルLLMを動かしてみた話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 01:31
- **URL**: [https://zenn.dev/sumasate_tec/articles/test-local-llm](https://zenn.dev/sumasate_tec/articles/test-local-llm)

## 概要

はじめに
スマサテでWebアプリケーション開発を担当している上田です。
普段の開発では Claude Code を使っていますが、便利な反面使っていると気になってくるのが使用量です。調査で大量のファイルを読ませたり、同じ作業を何度もやり直させたりすると、それなりに消費します。
そんなときに知ったのが MiniCPM5 という軽量なモデルです。2B クラスと小さく、手元のPCで動かすことを前提にコーディングエージェントやツール呼び出しにも使えると紹介されていました。
手元のPCで動くなら Claude Code の作業の一部をローカルLLMに任せて使用量を抑えられるのでは？と考えて、会...

---

*この記事は自動収集システムによって保存されました。*
