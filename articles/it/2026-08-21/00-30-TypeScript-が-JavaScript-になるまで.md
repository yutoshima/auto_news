---
title: "TypeScript が JavaScript になるまで"
source: "Zenn"
category: "it"
published: 2026-08-21T00:30:05
url: https://zenn.dev/onclimb/articles/ts-to-js-pipeline-onclimb
---

# TypeScript が JavaScript になるまで

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月21日 00:30
- **URL**: [https://zenn.dev/onclimb/articles/ts-to-js-pipeline-onclimb](https://zenn.dev/onclimb/articles/ts-to-js-pipeline-onclimb)

## 概要

TypeScript で記載したプログラム（.ts）は、.js に変換されてから実行されます。毎日この変換のお世話になっているのに、中で何が起きているかは見たことがない — そんな方が多いのではないでしょうか？
筆者も「型チェックをした後、型を消して JS にしている」くらいの解像度で理解していました。ただ、あらためて考えると「チェックして、消す」の中身はまるごとブラックボックスです。そもそも .ts が .js になるまでに、どんなプロセスを踏んでいるのか。それが知りたくて、Express の Hello World という最小の題材を TypeScript 7.0.2 でコンパイルし...

---

*この記事は自動収集システムによって保存されました。*
