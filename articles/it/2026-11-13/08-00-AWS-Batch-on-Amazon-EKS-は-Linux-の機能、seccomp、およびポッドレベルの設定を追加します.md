---
title: "AWS Batch on Amazon EKS は Linux の機能、seccomp、およびポッドレベルの設定を追加します"
source: "AWS What's New"
category: "it"
published: 2026-11-13T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/
---

# AWS Batch on Amazon EKS は Linux の機能、seccomp、およびポッドレベルの設定を追加します

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月13日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/)

## 概要

AWS Batchは現在、Amazon EKSのジョブ定義における追加のKubernetesセキュリティコンテキスト設定をサポートしています。これにはLinuxの能力、seccompプロファイル、ポッドレベルの設定が含まれます。Kubernetes Pod Security Standardsの制限付きプロファイルを適用するEKSクラスターでは、必要な権限とシステムコールのみを持つAWS Batchジョブを実行できるようになりました。

開始するには、RegisterJobDefinition APIを使用して、コンテナのセキュア設定のcapabilitiesとseccompProfileを設定します。

---

*この記事は自動収集システムによって保存されました。*
