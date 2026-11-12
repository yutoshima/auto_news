---
title: "[アップデート] Amazon EKS Auto ModeでKubernetes Gateway APIが使えるようになりました"
source: "DevelopersIO"
category: "it"
published: 2026-11-11T17:59:07
url: https://dev.classmethod.jp/articles/eks-auto-mode-kubernetes-gateway-api/
---

# [アップデート] Amazon EKS Auto ModeでKubernetes Gateway APIが使えるようになりました

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月11日 17:59
- **URL**: [https://dev.classmethod.jp/articles/eks-auto-mode-kubernetes-gateway-api/](https://dev.classmethod.jp/articles/eks-auto-mode-kubernetes-gateway-api/)

## 概要

EKS Auto ModeがKubernetes Gateway APIに対応しました。クラスターの設定でGateway APIを有効にすれば、AWS Load Balancer Controllerを自分で入れなくても、GatewayやHTTPRouteを作成するだけでALBが作られます。今回は重み付けルーティングやACM証明書の自動検出などを実際に試した結果をまとめます。

---

*この記事は自動収集システムによって保存されました。*
