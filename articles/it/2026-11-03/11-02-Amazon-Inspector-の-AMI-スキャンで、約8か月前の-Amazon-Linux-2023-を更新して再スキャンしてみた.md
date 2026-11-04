---
title: "Amazon Inspector の AMI スキャンで、約8か月前の Amazon Linux 2023 を更新して再スキャンしてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-03T11:02:23
url: https://dev.classmethod.jp/articles/inspector-ami-scan-al2023-update/
---

# Amazon Inspector の AMI スキャンで、約8か月前の Amazon Linux 2023 を更新して再スキャンしてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 11:02
- **URL**: [https://dev.classmethod.jp/articles/inspector-ami-scan-al2023-update/](https://dev.classmethod.jp/articles/inspector-ami-scan-al2023-update/)

## 概要

Amazon Inspector の AMI スキャンで、3月版と11月版の AL2023 を比べました。検出は3月版が 3,161件、11月版が 0件でした。3月版を更新して作り直すと 2,743件に減りましたが、残りはすべて旧カーネル 6.18 の rpm で、旧カーネルを撤去して作り直すと 0件になりました。

---

*この記事は自動収集システムによって保存されました。*
