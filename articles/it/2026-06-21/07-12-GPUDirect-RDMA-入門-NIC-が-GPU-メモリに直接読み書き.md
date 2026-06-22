---
title: "GPUDirect RDMA 入門: NIC が GPU メモリに直接読み書き"
source: "Zenn"
category: "it"
published: 2026-06-21T07:12:02
url: https://zenn.dev/tosshi/articles/42f0ee03b328a4
---

# GPUDirect RDMA 入門: NIC が GPU メモリに直接読み書き

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月21日 07:12
- **URL**: [https://zenn.dev/tosshi/articles/42f0ee03b328a4](https://zenn.dev/tosshi/articles/42f0ee03b328a4)

## 概要

はじめに
!
この記事のゴール: 「GPU 同士がネットワーク越しに、CPU をほとんど介さず直接データをやり取りする」仕組みである GPUDirect RDMA を、初学者向けに解説します。

そもそも RDMA とは何か（Buffer → NIC → NIC → Buffer）
TCP/IP と何が違うのか（RTT・カーネルバイパス）
RDMA の操作（RDMA Operations）と「メモリ登録」
GPUDirect RDMA — NIC が GPU メモリに直接アクセスする（2 つの実現方式）
AWS EFA はどうやって RDMA を実現しているか（SRD / Queue...

---

*この記事は自動収集システムによって保存されました。*
