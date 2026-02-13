---
title: "octorusはなぜ30万行のdiffを高速表示できるのか？"
source: "Zenn"
category: "it"
published: 2026-02-13T02:24:59
url: https://zenn.dev/ushironoko/articles/ae9fa49dd18515
---

# octorusはなぜ30万行のdiffを高速表示できるのか？

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月13日 02:24
- **URL**: [https://zenn.dev/ushironoko/articles/ae9fa49dd18515](https://zenn.dev/ushironoko/articles/ae9fa49dd18515)

## 概要

https://zenn.dev/ushironoko/articles/90d34dd61a1825
以前上記で、自作しているtuiツールを紹介しました。
需要があるかわかりませんが、今回はoctorusで行っているパフォーマンス最適化について紹介します。
https://github.com/ushironoko/octorus

 そもそも何が速いのか？
「速い」といっても色々あります。表示ひとつとっても、初回表示の速さやハイライトを当てる速さ、スクロールのスムーズさ（fps）など多様です。
ユーザーの体感速度の速さと、内部的な速さは必ずしもイコールにはなりません。例えばどれだけゼ...

---

*この記事は自動収集システムによって保存されました。*
