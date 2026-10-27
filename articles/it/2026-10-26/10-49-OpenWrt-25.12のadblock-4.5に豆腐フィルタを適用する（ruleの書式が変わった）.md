---
title: "OpenWrt 25.12のadblock 4.5に豆腐フィルタを適用する（ruleの書式が変わった）"
source: "Zenn"
category: "it"
published: 2026-10-26T10:49:33
url: https://zenn.dev/yotan/articles/openwrt-25-adblock-tofu-filter
---

# OpenWrt 25.12のadblock 4.5に豆腐フィルタを適用する（ruleの書式が変わった）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月26日 10:49
- **URL**: [https://zenn.dev/yotan/articles/openwrt-25-adblock-tofu-filter](https://zenn.dev/yotan/articles/openwrt-25-adblock-tofu-filter)

## 概要

はじめに
自宅のDNSとDHCPを担当しているルーターを、OpenWrt 24.10から25.12.6の別機に入れ替えました。その準備の途中で、adblockに豆腐フィルタを追加するカスタムフィードの書式が変わっていて、旧機の設定をそのまま写すだけでは、ブロックが働きませんでした。直したあとも、旧機と比べると差があり、X（旧Twitter）やLINEまで止まっていました。
以前に書いた OpenWrt 22.03のadblockに豆腐フィルタを適用する の続編です。adblock 4.5.9での書き方と、ハマった点をまとめます。
先に結論です。

adblock 4.4のawk式の ...

---

*この記事は自動収集システムによって保存されました。*
