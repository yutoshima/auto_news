---
title: "AWS Network Firewallのコンテナ関連付け（Container Association）を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-30T04:33:51
url: https://dev.classmethod.jp/articles/202610-network-firewall-container-association-eks/
---

# AWS Network Firewallのコンテナ関連付け（Container Association）を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月30日 04:33
- **URL**: [https://dev.classmethod.jp/articles/202610-network-firewall-container-association-eks/](https://dev.classmethod.jp/articles/202610-network-firewall-container-association-eks/)

## 概要

EKSやECSで稼働するコンテナのIPアドレスの一覧を、Network Firewallのルールから参照できる機能です。EKSのPodをnamespaceやラベルで選択し、アプリケーションごとに接続先のドメインを制限するルールを構成して動作を確認しました。

---

*この記事は自動収集システムによって保存されました。*
