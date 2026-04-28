---
title: "Claude Codeのルーチン機能で定期的にパフォーマンスチューニングをさせている"
source: "Zenn"
category: "it"
published: 2026-04-28T02:16:45
url: https://zenn.dev/yamadashy/articles/claude-code-routines-perf-tuning
---

# Claude Codeのルーチン機能で定期的にパフォーマンスチューニングをさせている

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月28日 02:16
- **URL**: [https://zenn.dev/yamadashy/articles/claude-code-routines-perf-tuning](https://zenn.dev/yamadashy/articles/claude-code-routines-perf-tuning)

## 概要

Claude Codeのルーチン（Routines）機能を、何に使うのが良いのかしばらく考えていました。
クラウド上でプロンプトを定期実行できる便利な機能なのですが、定期的に動かして意味のあるタスクは何だろう、と。
たどり着いたのが、パフォーマンスチューニングです。
「速くなったか」は数値で判断できるので、ベンチマーク基盤さえあれば、あとはAIに任せられます。
機能としてデグレしていないかもテストが充実していれば自動で確認できますし、ブランチを切って進めるので本流には影響しません。設計の創造性があまり要らないのもAIに任せやすいところですね。
私が開発しているRepomixというCLIで...

---

*この記事は自動収集システムによって保存されました。*
