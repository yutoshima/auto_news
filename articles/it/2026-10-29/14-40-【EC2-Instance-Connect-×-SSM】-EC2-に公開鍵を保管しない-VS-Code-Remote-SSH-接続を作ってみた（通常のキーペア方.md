---
title: "【EC2 Instance Connect × SSM】 EC2 に公開鍵を保管しない VS Code Remote - SSH 接続を作ってみた（通常のキーペア方式と比較）"
source: "DevelopersIO"
category: "it"
published: 2026-10-29T14:40:02
url: https://dev.classmethod.jp/articles/ec2-instance-connect-ssm-vscode-remote-ssh/
---

# 【EC2 Instance Connect × SSM】 EC2 に公開鍵を保管しない VS Code Remote - SSH 接続を作ってみた（通常のキーペア方式と比較）

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月29日 14:40
- **URL**: [https://dev.classmethod.jp/articles/ec2-instance-connect-ssm-vscode-remote-ssh/](https://dev.classmethod.jp/articles/ec2-instance-connect-ssm-vscode-remote-ssh/)

## 概要

SSM Session Manager経由でプライベートサブネットのEC2にVS Codeで接続する際、EC2 Instance Connectを使って公開鍵を一時登録する方法を試しました。通常のキーペア方式との違いや、セットアップ手順を紹介します。

---

*この記事は自動収集システムによって保存されました。*
