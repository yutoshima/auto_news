---
title: "HonoのNode.jsアダプタが最大2.3倍速くなります"
source: "Zenn"
category: "it"
published: 2026-04-17T03:07:25
url: https://zenn.dev/yusukebe/articles/9dce6cf7dc6e41
---

# HonoのNode.jsアダプタが最大2.3倍速くなります

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月17日 03:07
- **URL**: [https://zenn.dev/yusukebe/articles/9dce6cf7dc6e41](https://zenn.dev/yusukebe/articles/9dce6cf7dc6e41)

## 概要

これからリリースするHonoのNode.jsアダプタのv2では、ボディパースのベンチマークで従来のv1系と比べて2.3倍速くなります。
近日中にリリースしますが、現在RC版が使えるので試してみてください。
npm i @hono/node-server@2.0.0-rc.2

 v2
Node.jsアダプタはメジャーバージョンアップをしてv2系になります。といってもメインのAPIは変わらず、これから紹介する大幅なパフォーマンス向上が目玉となります。他の変更点はNode.js v18系のサポートを切ることと不要になったVercel用のアダプタをobsoleteにします。

 Node.js...

---

*この記事は自動収集システムによって保存されました。*
