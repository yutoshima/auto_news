---
title: "PRを送るだけでリポジトリを「乗っ取れる」？GitHub Actionsの危ない書き方を実際に検証してみた (hackerbot-claw)"
source: "Zenn"
category: "it"
published: 2026-03-03T00:37:27
url: https://zenn.dev/aeyesec/articles/417578718dcced
---

# PRを送るだけでリポジトリを「乗っ取れる」？GitHub Actionsの危ない書き方を実際に検証してみた (hackerbot-claw)

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年03月03日 00:37
- **URL**: [https://zenn.dev/aeyesec/articles/417578718dcced](https://zenn.dev/aeyesec/articles/417578718dcced)

## 概要

こんにちは！エーアイセキュリティラボのはるぷです。
2026年2月下旬、オープンソース界隈を揺るがす自動攻撃キャンペーンが実施されました。ターゲットとなったのは、誰もが名前を知るような大手企業のプロジェクトを含む主要なリポジトリ群。攻撃の主導者は 「hackerbot-claw」 と呼ばれる、AI（Claude-Opus-4.5）を搭載した自律型セキュリティ調査エージェントです。
このボットはわずか1週間で、7つのターゲットのうち少なくとも4つでリモートコード実行（RCE）に成功し、書き込み権限を持つGitHubトークンを外部へ流出させました。
このStepSecurityの解析レポート...

---

*この記事は自動収集システムによって保存されました。*
