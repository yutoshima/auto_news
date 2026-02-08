---
title: "AWSインフラ設計のベストプラクティスを目指して(IaC編)"
source: "Zenn"
category: "it"
published: 2026-02-07T06:58:24
url: https://zenn.dev/so_engineer/articles/45acac4e572ff3
---

# AWSインフラ設計のベストプラクティスを目指して(IaC編)

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年02月07日 06:58
- **URL**: [https://zenn.dev/so_engineer/articles/45acac4e572ff3](https://zenn.dev/so_engineer/articles/45acac4e572ff3)

## 概要

はじめに
Terraformを用いてAWSの各リソースをコード化しました。
以前まとめた記事の構成図の各リソースが主な対象になります。


なお、赤点線枠はTerraformでは管理しづらいことから、ecspressoで管理しています。


 モジュール群

リソースごとに抽象化し、複数の環境で同じ構成を実現するために使う
AWSのサービス単位で作ると運用しやすい
モジュール内は過度な抽象化は避け、基本はベタ書き推奨
とはいえあまりに繰り返しが多い箇所はunit moduleを作る

※unit moduleはモジュールのモジュールのこと。基本はaws.tfからモジュールAを参照する...

---

*この記事は自動収集システムによって保存されました。*
