---
title: "Amazon CloudWatch エージェントが journald ログのサポートを追加しました"
source: "AWS What's New"
category: "it"
published: 2026-08-28T16:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-agent-journald/
---

# Amazon CloudWatch エージェントが journald ログのサポートを追加しました

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年08月28日 16:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-agent-journald/](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-agent-journald/)

## 概要

AWSは、Amazon CloudWatchエージェントを使用してsystemdジャーナル（journald）ログを収集するサポートを発表しました。これにより、Linuxインスタンス上のsystemdジャーナルから直接ログエントリを読み取り、まずディスク上のファイルへ書き出すことなく、CloudWatch Logsへ送信するようCloudWatchエージェントを構成できます。

多くの現代的なLinuxディストリビューション（Amazon Linux 2023を含む）は、systemdジャーナルを主要なログシステムとして使用しており、従来のテキストログファイル（例：/var/log/me...）を以前のように書き出さなくなっています。

---

*この記事は自動収集システムによって保存されました。*
