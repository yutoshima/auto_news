---
title: "Bun が 6 日で Rust に書き換わった件"
source: "Zenn"
category: "it"
published: 2026-05-15T06:08:40
url: https://zenn.dev/ashunar0/articles/55a669c10e6a8d
---

# Bun が 6 日で Rust に書き換わった件

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月15日 06:08
- **URL**: [https://zenn.dev/ashunar0/articles/55a669c10e6a8d](https://zenn.dev/ashunar0/articles/55a669c10e6a8d)

## 概要

はじめに
2026年5月14日、JavaScript ランタイム Bun の Zig→Rust 大規模移植 PR が main ブランチにマージされた。約 96 万行のコードを、6 日間で、AI（Claude）が書いた。テストは 99.8% パス、バイナリサイズも縮小されているが、unsafe ブロックは 13,000 箇所を超え、Sumner 本人も「全部破棄する可能性が高い」と発言している。
この一連の動きを追いかけながら、初見で抱いた 5 つの素朴な疑問 を整理した。


 まず、何が起きたか
時系列で圧縮するとこうなる。


2026/05/05：Bun 創業者 Jarred...

---

*この記事は自動収集システムによって保存されました。*
