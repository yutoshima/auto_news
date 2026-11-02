---
title: "Cloudflare Workersを触ってみた"
source: "Zenn"
category: "it"
published: 2026-10-30T05:01:51
url: https://zenn.dev/atware/articles/ec1dfd799289b7
---

# Cloudflare Workersを触ってみた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月30日 05:01
- **URL**: [https://zenn.dev/atware/articles/ec1dfd799289b7](https://zenn.dev/atware/articles/ec1dfd799289b7)

## 概要

はじめに
普段の開発ではAWSを使うことが多いのですが、Cloudflareの全体像を調べてみた記事を書いた際に、アプリケーション実行基盤である Cloudflare Workers にとても興味を持ちました。
CloudflareというとCDNのイメージが強かったのですが、Workersを使うとエッジ上でJavaScript / TypeScriptを使ってAPIまで動かせます。公式チュートリアルを参考に、Reactの画面とAPIを1つのWorkerで作り、デプロイしてIP制限をかけるところまで試してみました。
今回は、実際に手を動かしてみて分かったことや、その過程で気になった点を...

---

*この記事は自動収集システムによって保存されました。*
