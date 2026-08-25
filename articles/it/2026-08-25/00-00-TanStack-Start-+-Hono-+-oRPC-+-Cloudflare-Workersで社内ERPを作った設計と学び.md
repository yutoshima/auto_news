---
title: "TanStack Start + Hono + oRPC + Cloudflare Workersで社内ERPを作った設計と学び"
source: "Zenn"
category: "it"
published: 2026-08-25T00:00:05
url: https://zenn.dev/yosashusaku/articles/enterprise-erp-tanstack-hono-orpc
---

# TanStack Start + Hono + oRPC + Cloudflare Workersで社内ERPを作った設計と学び

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年08月25日 00:00
- **URL**: [https://zenn.dev/yosashusaku/articles/enterprise-erp-tanstack-hono-orpc](https://zenn.dev/yosashusaku/articles/enterprise-erp-tanstack-hono-orpc)

## 概要

はじめに
建築業向けの社内ERP（プロジェクト管理・CRM・工数管理・ダッシュボード）を、Full-Stack TypeScriptでスクラッチ開発しました。TanStack Start + Hono + oRPCを、Cloudflare Workersの上で動かしています。
この構成はまだ事例が少なく、「動くところまでは書けるが、業務システムのサイズに育ったときにどうなるのか」が想像しづらい領域だと思います。この記事はスタックの紹介ではなく、どこに境界を引いたのか／引き直したのかの話です。
結論を先に並べると、主な判断はこの4つです。



判断
採用
主な理由




実行基盤
...

---

*この記事は自動収集システムによって保存されました。*
