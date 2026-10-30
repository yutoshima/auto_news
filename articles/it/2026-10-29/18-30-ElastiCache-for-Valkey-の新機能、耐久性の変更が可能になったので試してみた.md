---
title: "ElastiCache for Valkey の新機能、耐久性の変更が可能になったので試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-29T18:30:05
url: https://dev.classmethod.jp/articles/elasticache-valkey-durability-change/
---

# ElastiCache for Valkey の新機能、耐久性の変更が可能になったので試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月29日 18:30
- **URL**: [https://dev.classmethod.jp/articles/elasticache-valkey-durability-change/](https://dev.classmethod.jp/articles/elasticache-valkey-durability-change/)

## 概要

Amazon ElastiCache for Valkey で、既存クラスターの耐久性を作り直さずに変更できるようになりました。Valkey 9.0 で試すと、有効化・無効化はフェイルオーバーを伴って約14分半〜約20分かかり、非同期から同期への変更は available のまま短時間で終わりました。

---

*この記事は自動収集システムによって保存されました。*
