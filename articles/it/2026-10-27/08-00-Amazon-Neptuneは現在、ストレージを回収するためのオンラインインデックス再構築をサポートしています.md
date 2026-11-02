---
title: "Amazon Neptuneは現在、ストレージを回収するためのオンラインインデックス再構築をサポートしています"
source: "AWS What's New"
category: "it"
published: 2026-10-27T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/10/neptune-online-index-rebuild/
---

# Amazon Neptuneは現在、ストレージを回収するためのオンラインインデックス再構築をサポートしています

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年10月27日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/10/neptune-online-index-rebuild/](https://aws.amazon.com/about-aws/whats-new/2026/10/neptune-online-index-rebuild/)

## 概要

<ahref="https://aws.amazon.com/neptune/">Amazon Neptune</a> データベースは現在、オンラインインデックス再構築をサポートしています。これは、データベースをオフラインにすることなく、Neptune のインデックスをデフラグし、未使用のストレージ領域を回収する新しい機能です。時間の経過とともに、挿入、更新、削除操作がデータページ内に未使用スペースのギャップを作り出し、データが削除された後でも <code>VolumeBytesUsed</code> 指標が人工的に高い状態のままになることがあります。この断片化は増大します。

---

*この記事は自動収集システムによって保存されました。*
