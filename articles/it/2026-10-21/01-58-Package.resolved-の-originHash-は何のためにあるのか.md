---
title: "Package.resolved の originHash は何のためにあるのか"
source: "Zenn"
category: "it"
published: 2026-10-21T01:58:50
url: https://zenn.dev/zunda_pixel/articles/ecba94910fa062
---

# Package.resolved の originHash は何のためにあるのか

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月21日 01:58
- **URL**: [https://zenn.dev/zunda_pixel/articles/ecba94910fa062](https://zenn.dev/zunda_pixel/articles/ecba94910fa062)

## 概要

Renovate が依存を上げた PR をマージしたあと、tuist install を流すと Package.resolved の 1 行だけが書き換わるようになりました。

Package.resolved
 {
-  "originHash" : "b51d86e0d60dc9c07d7da15f1bb995c680b75f60f09f0ee586aea8f14852849d",
+  "originHash" : "9ea100c33d0673a7cbf638a61115d34ce142720e95d1761c390aa31ae6ec796b",
   "pins" : [

こ...

---

*この記事は自動収集システムによって保存されました。*
