---
title: "図で理解する Plan 9 アセンブリと Go の中の Plan 9"
source: "Zenn"
category: "it"
published: 2026-06-30T00:46:57
url: https://zenn.dev/jamesbob/articles/plan9_go_assembly_zenn
---

# 図で理解する Plan 9 アセンブリと Go の中の Plan 9

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月30日 00:46
- **URL**: [https://zenn.dev/jamesbob/articles/plan9_go_assembly_zenn](https://zenn.dev/jamesbob/articles/plan9_go_assembly_zenn)

## 概要

Goで .s ファイルを書くと、TEXT ·Add(SB), NOSPLIT, $0-24 のような見慣れない記法に出会います。これは「Plan 9というOSそのものを使っている」という意味ではなく、Plan 9系アセンブラの入力スタイルを受け継いだ、Go専用アセンブラを使うという意味です。[1]
この記事では、細かい命令表よりも「なぜそう見えるのか」を図でつかみます。

 この記事の地図

 Plan 9とは
Plan 9は、UnixやC言語を生んだBell Labsで1980年代後半から開発された研究用OSです。中心にある発想は「分散環境でも、資源をファイルのように扱えるようにする」...

---

*この記事は自動収集システムによって保存されました。*
