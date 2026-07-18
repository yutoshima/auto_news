---
title: "個人開発のLaravelサイトにOpenTelemetry+Grafanaで可観測性基盤を作った（Docker無し・systemd運用）"
source: "Zenn"
category: "it"
published: 2026-07-18T04:26:35
url: https://zenn.dev/shim_03248/articles/5094579401a468
---

# 個人開発のLaravelサイトにOpenTelemetry+Grafanaで可観測性基盤を作った（Docker無し・systemd運用）

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月18日 04:26
- **URL**: [https://zenn.dev/shim_03248/articles/5094579401a468](https://zenn.dev/shim_03248/articles/5094579401a468)

## 概要

はじめに
個人で運営しているPHP8技術者認定初級試験の模擬試験サイト（Laravel製）に、OpenTelemetry + Grafanaスタックで可観測性基盤を構築しました。

アプリコードほぼ変更なし（ゼロコード自動計装）
本番はDockerを使わず、全部バイナリ + systemd

可視化は日本語UIのGrafanaに一元化（Jaegerは採用を見送った理由も後述）
ロールバックは環境変数1つで完結

という構成です。単一VPSで運用する個人開発サイトを想定した内容ですが、小規模チームのLaravelアプリでもそのまま使えるはずです。実際に詰まったポイント（.envに書いて...

---

*この記事は自動収集システムによって保存されました。*
