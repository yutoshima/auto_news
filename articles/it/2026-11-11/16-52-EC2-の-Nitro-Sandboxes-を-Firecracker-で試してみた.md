---
title: "EC2 の Nitro Sandboxes を Firecracker で試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-11T16:52:52
url: https://dev.classmethod.jp/articles/nitro-sandboxes-ec2-firecracker/
---

# EC2 の Nitro Sandboxes を Firecracker で試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月11日 16:52
- **URL**: [https://dev.classmethod.jp/articles/nitro-sandboxes-ec2-firecracker/](https://dev.classmethod.jp/articles/nitro-sandboxes-ec2-firecracker/)

## 概要

EC2 の Nitro Sandboxes で、Firecracker の sandbox を 2 台起動し、メモリ、ストレージ、ネットワークの隔離を確認しました。confidential モードでは、親の root でもゲストのメモリを読めませんでした。ストレージは親から読め、IMDS と VM 間の通信は親の nftables で止めました。

---

*この記事は自動収集システムによって保存されました。*
