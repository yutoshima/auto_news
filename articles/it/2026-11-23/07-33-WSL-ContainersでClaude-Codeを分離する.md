---
title: "WSL ContainersでClaude Codeを分離する"
source: "Zenn"
category: "it"
published: 2026-11-23T07:33:06
url: https://zenn.dev/kent_code/articles/bef81d6a0b817c
---

# WSL ContainersでClaude Codeを分離する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 07:33
- **URL**: [https://zenn.dev/kent_code/articles/bef81d6a0b817c](https://zenn.dev/kent_code/articles/bef81d6a0b817c)

## 概要

Claude Code に許可を求められたとき、よく読まずに Yes を押したことはありませんか。
恥ずかしながら自分はよくあります。
その Yes 1回で何が起きるのでしょうか。Claude Code は、起動したフォルダ（以下、作業フォルダ）の中で作業するのが基本です。Yes と答えれば、作業フォルダの外のファイルも読めたり、ファイルを消したり、外へ送ったりもできてしまう可能性があります。
試しに、作業フォルダの外にダミーの秘密ファイルを置いて、Claude Code に読ませてみました。確認の画面は出ましたが、最初から選ばれているのは「今後もずっと許可」で、Yes を1回選ぶ（En...

---

*この記事は自動収集システムによって保存されました。*
