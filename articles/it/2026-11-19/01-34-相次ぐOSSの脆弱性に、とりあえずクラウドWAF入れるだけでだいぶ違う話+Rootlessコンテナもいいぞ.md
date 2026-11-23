---
title: "相次ぐOSSの脆弱性に、とりあえずクラウドWAF入れるだけでだいぶ違う話+Rootlessコンテナもいいぞ"
source: "Zenn"
category: "it"
published: 2026-11-19T01:34:24
url: https://zenn.dev/kusuke/articles/98e178e6824cac
---

# 相次ぐOSSの脆弱性に、とりあえずクラウドWAF入れるだけでだいぶ違う話+Rootlessコンテナもいいぞ

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 01:34
- **URL**: [https://zenn.dev/kusuke/articles/98e178e6824cac](https://zenn.dev/kusuke/articles/98e178e6824cac)

## 概要

昨日から今日にかけて、なんだかすごいことになっていますね。
先日「PHP2Shell（CVE-2026-109618 / CVE-2026-109619）」というコアそのもののRCE（リモートコード実行）が出て大騒ぎになったと思ったら、JavaでもJavaのBase64デコーダ周りで「Java2Shell（CVE-2026-114938）」が出てきました。さらに今日（11月18日・米国時間）はnginxで10年前から潜んでいたHTTP/2のメモリ破壊バグ（CVE-2026-123007、通称nginx2rootなど）が発表され、今晩23時からはPHPのCriticalな脆弱性リリースまで...

---

*この記事は自動収集システムによって保存されました。*
