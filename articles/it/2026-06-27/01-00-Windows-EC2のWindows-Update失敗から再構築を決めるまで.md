---
title: "Windows EC2のWindows Update失敗から再構築を決めるまで"
source: "Zenn"
category: "it"
published: 2026-06-27T01:00:00
url: https://zenn.dev/yamadatt/articles/20260627-windows-ec2-update-rebuild
---

# Windows EC2のWindows Update失敗から再構築を決めるまで

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月27日 01:00
- **URL**: [https://zenn.dev/yamadatt/articles/20260627-windows-ec2-update-rebuild](https://zenn.dev/yamadatt/articles/20260627-windows-ec2-update-rebuild)

## 概要

はじめに
EC2上のWindows Server 2025に、2026年6月のWindows Updateで配信された 2026-06 Security Update (KB5094125) (26100.32995) を適用しようとしたところ、この累積更新プログラムだけが何度実行しても失敗しました。
普段からWindows Serverを触っているわけではないため、Windows Update、CBS、DISM、SFC、イベントログなどを都度調べながら進めました。
遠回りした部分もありますが、どの確認を行い、どこで再構築に切り替えたのかを後から追えるように、試した修復やログから分か...

---

*この記事は自動収集システムによって保存されました。*
