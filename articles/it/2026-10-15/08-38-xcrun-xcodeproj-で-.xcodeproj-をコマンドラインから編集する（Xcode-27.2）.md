---
title: "xcrun xcodeproj で .xcodeproj をコマンドラインから編集する（Xcode 27.2）"
source: "Zenn"
category: "it"
published: 2026-10-15T08:38:00
url: https://zenn.dev/d_date/articles/xcrun-xcodeproj-xcode27-2
---

# xcrun xcodeproj で .xcodeproj をコマンドラインから編集する（Xcode 27.2）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 08:38
- **URL**: [https://zenn.dev/d_date/articles/xcrun-xcodeproj-xcode27-2](https://zenn.dev/d_date/articles/xcrun-xcodeproj-xcode27-2)

## 概要

はじめに
Xcode 27.2 には、xcrun xcodeproj というコマンドラインツールが同梱されています。Beta 2 の時点では setting / target / group の 3 つのサブコマンドだけでしたが、Beta 3 では init / config / pkg などが加わり、プロジェクトの作成からパッケージ依存の管理までできるようになりました。
$ xcrun xcodeproj --help
OVERVIEW: Inspect and modify Xcode project files (.xcodeproj) from the command
lin...

---

*この記事は自動収集システムによって保存されました。*
