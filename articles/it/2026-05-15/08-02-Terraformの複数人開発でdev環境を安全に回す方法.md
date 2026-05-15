---
title: "Terraformの複数人開発でdev環境を安全に回す方法"
source: "Zenn"
category: "it"
published: 2026-05-15T08:02:00
url: https://zenn.dev/pksha/articles/terraform-multi-user-apply-conflict
---

# Terraformの複数人開発でdev環境を安全に回す方法

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月15日 08:02
- **URL**: [https://zenn.dev/pksha/articles/terraform-multi-user-apply-conflict](https://zenn.dev/pksha/articles/terraform-multi-user-apply-conflict)

## 概要

はじめに
こんにちは、PKSHA Technology で SRE をしている柴田です。
Terraform を複数人で運用しているチームで、こんな悩みはありませんか？

自分の apply した変更が、別メンバーの apply で消えてしまう

-target で影響範囲を絞っても、他のメンバーの変更が差分として出てしまう

Terraform の複数人運用について検索すると、state ファイルの共有や lock の話はたくさん出てきます。一方で、shared な dev 環境で複数人が同時に検証するとき、ブランチごとに異なる変更をどう扱うかという観点の記事は、あまり見かけません...

---

*この記事は自動収集システムによって保存されました。*
