---
title: "【PDF圧縮】約40年続く業界標準Ghostscriptを、Rust 自前実装で抜いた話"
source: "Zenn"
category: "it"
published: 2026-05-21T05:50:24
url: https://zenn.dev/ikora/articles/b50ca6275eddc9
---

# 【PDF圧縮】約40年続く業界標準Ghostscriptを、Rust 自前実装で抜いた話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月21日 05:50
- **URL**: [https://zenn.dev/ikora/articles/b50ca6275eddc9](https://zenn.dev/ikora/articles/b50ca6275eddc9)

## 概要

はじめに
皆さん如何お過ごしでしょうか？
最近はどの技術記事もAI一色で食傷気味の長嶋です。
さて本日は、個人開発しているデスクトップアプリ Karui に PDF 圧縮機能を載せてみたら意外と深い穴にハマったので、 その記録です。
https://karui.app/ja
ちなみにこのKaruiは Tauri v2で実装されており、Win/Mac両対応のデスクトップ画像圧縮アプリです。Tauriについては以前の記事で書いております。
https://zenn.dev/genshi_ai/articles/fa96e541c480d2
そして最初に結論。

8 種類のテスト PDF（...

---

*この記事は自動収集システムによって保存されました。*
