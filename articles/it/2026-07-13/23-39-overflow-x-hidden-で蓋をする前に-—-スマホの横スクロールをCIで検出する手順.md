---
title: "overflow-x hidden で蓋をする前に — スマホの横スクロールをCIで検出する手順"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-13T23:39:58
url: https://qiita.com/masakazuimai/items/bcc721ad6820329dd6a5
---

# overflow-x hidden で蓋をする前に — スマホの横スクロールをCIで検出する手順

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月13日 23:39
- **URL**: [https://qiita.com/masakazuimai/items/bcc721ad6820329dd6a5](https://qiita.com/masakazuimai/items/bcc721ad6820329dd6a5)

## 概要

この記事でやること
スマホ幅で横スクロールが出たとき、body { overflow-x: hidden; } で塞ぐのは対症療法です。原因の要素は残ったままなので、次の実装でまた混入します。
この記事では、横スクロールの原因要素を特定し、その検出をPlaywrightで...

---

*この記事は自動収集システムによって保存されました。*
