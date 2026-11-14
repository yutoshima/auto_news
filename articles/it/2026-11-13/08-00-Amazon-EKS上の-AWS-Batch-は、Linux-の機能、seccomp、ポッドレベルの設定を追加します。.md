---
title: "Amazon EKS上の AWS Batch は、Linux の機能、seccomp、ポッドレベルの設定を追加します。"
source: "AWS What's New"
category: "it"
published: 2026-11-13T08:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/
---

# Amazon EKS上の AWS Batch は、Linux の機能、seccomp、ポッドレベルの設定を追加します。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年11月13日 08:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/)

## 概要

AWS Batchは、Linuxの機能、seccompプロファイル、およびPodレベルの設定を含む、Amazon EKSのジョブ定義に対する追加のKubernetesセキュリティコンテキスト設定をサポートするようになりました。Kubernetes Pod Security Standardsのrestrictedプロファイルを適用するEKSクラスターでは、必要な権限とシステムコールのみを持つAWS Batchのジョブを実行できます。

開始するには、RegisterJobDefinition APIを使用して、コンテナのsecur内のcapabilitiesとseccompProfileを設定します。

---

*この記事は自動収集システムによって保存されました。*
