---
title: "他社AIエージェントの会話ログを自動でVaultに取り込む ― Manus APIブリッジの設計"
source: "Qiita (Python)"
category: "it"
published: 2026-09-25T23:18:17
url: https://qiita.com/bokuwalily/items/909f5d8be2cd3b16a761
---

# 他社AIエージェントの会話ログを自動でVaultに取り込む ― Manus APIブリッジの設計

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年09月25日 23:18
- **URL**: [https://qiita.com/bokuwalily/items/909f5d8be2cd3b16a761](https://qiita.com/bokuwalily/items/909f5d8be2cd3b16a761)

## 概要

前回、スキルCLIの週次バッチが黙って失敗していた話を書きました。今回は同じVault運用の続きで、Claude Code以外のAIエージェント（Manus）の会話を、API経由で共有Vaultの一次資料として自動収集する仕組みの話です。

困りごと：Manusのタスクだけ...

---

*この記事は自動収集システムによって保存されました。*
