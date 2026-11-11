---
title: "Azure BlobのSASを期限前に止めると、ほかのURLはどうなる？6本のSASで失効の範囲を確かめた"
source: "DevelopersIO"
category: "it"
published: 2026-11-10T11:22:28
url: https://dev.classmethod.jp/articles/azure-blob-sas-revocation/
---

# Azure BlobのSASを期限前に止めると、ほかのURLはどうなる？6本のSASで失効の範囲を確かめた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 11:22
- **URL**: [https://dev.classmethod.jp/articles/azure-blob-sas-revocation/](https://dev.classmethod.jp/articles/azure-blob-sas-revocation/)

## 概要

Azure BlobのSASを期限前に止める3つの操作を、種類の違う6本のSASで確かめました。操作ごとに、どのURLが一緒に止まり、反映に何秒かかったかを示します。そのうえで、配布先ごとに止めたいときにSASをどう発行するかを考えます。

---

*この記事は自動収集システムによって保存されました。*
