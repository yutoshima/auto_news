---
title: "@napi-rs/canvas v1.0.12 で実質的な破壊的変更が入った話"
source: "Zenn"
category: "it"
published: 2026-10-24T15:28:06
url: https://zenn.dev/devuloper/articles/napi_rs_canvas_1_0_12_font_tofu
---

# @napi-rs/canvas v1.0.12 で実質的な破壊的変更が入った話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月24日 15:28
- **URL**: [https://zenn.dev/devuloper/articles/napi_rs_canvas_1_0_12_font_tofu](https://zenn.dev/devuloper/articles/napi_rs_canvas_1_0_12_font_tofu)

## 概要

@napi-rs/canvas を 1.0.11 から 1.0.12 以降に上げると、ctx.font = '48px M PLUS Rounded 1c' のように引用符なしで書いたフォント指定が、まるごと無視されるようになりました。日本語は 10px の豆腐で描かれ、例外も警告も出ません。フォント名を "M PLUS Rounded 1c" のように引用符で囲めば直ります。
この記事は、気づいたきっかけから原因の特定、対策までをまとめたものです。

 きっかけ
makeitaquote は、メッセージから Make it a Quote 風の引用画像を作る自作の npm ライブラリで...

---

*この記事は自動収集システムによって保存されました。*
