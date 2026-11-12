---
title: "脆弱性の影響調査を Devin Automations で自動化した話"
source: "はてブ テクノロジー"
category: "it"
published: 2026-11-11T13:16:39
url: https://zenn.dev/rescuenow/articles/2ee1c4b66ecec8
---

# 脆弱性の影響調査を Devin Automations で自動化した話

## メタデータ

- **情報源**: はてブ テクノロジー
- **カテゴリ**: it
- **公開日時**: 2026年11月11日 13:16
- **URL**: [https://zenn.dev/rescuenow/articles/2ee1c4b66ecec8](https://zenn.dev/rescuenow/articles/2ee1c4b66ecec8)

## 概要

処理の流れは、毎日の定期実行と Slack からの依頼の 2 本です。 定期実行: 新着 CVE 登録 毎日の定期実行で Devin Automation が起動し、次の 2 つを行います。 登録: 直近 48 時間に NVD で公開された CVSS 一定以上の CVE のうち、 Notion データベースに未登録であれば登録する 更新: 登録済みの CVE で CVSS が前回...

---

*この記事は自動収集システムによって保存されました。*
