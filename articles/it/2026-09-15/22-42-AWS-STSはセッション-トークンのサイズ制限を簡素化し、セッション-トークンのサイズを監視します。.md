---
title: "AWS STSはセッション トークンのサイズ制限を簡素化し、セッション トークンのサイズを監視します。"
source: "AWS What's New"
category: "it"
published: 2026-09-15T22:42:00
url: https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts/
---

# AWS STSはセッション トークンのサイズ制限を簡素化し、セッション トークンのサイズを監視します。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年09月15日 22:42
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts/](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts/)

## 概要

AWS Security Token Service（STS）は、セッション・トークンのサイズに対して現在4,096バイトの単一制限を課しています。以前は、STSはセッション・トークンのサイズと渡し入れられたパラメータ（インライン・ポリシー、管理ポリシー、セッション・タグ）に別々の制限を適用していました。STSはその区分を廃止し、セッション・ポリシーとセッション・タグの組み合わせをより大きく柔軟に取り扱えるようにしました。

また、STSはセッション・トークンのサイズと、全体に対する利用率のパーセンテージを示すレスポンス要素を返すようになりました。

---

*この記事は自動収集システムによって保存されました。*
