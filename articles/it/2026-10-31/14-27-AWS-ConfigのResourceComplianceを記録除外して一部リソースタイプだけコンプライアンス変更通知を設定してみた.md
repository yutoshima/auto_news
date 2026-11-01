---
title: "AWS ConfigのResourceComplianceを記録除外して一部リソースタイプだけコンプライアンス変更通知を設定してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-31T14:27:42
url: https://dev.classmethod.jp/articles/config-resourcecompliance-scoped-notification/
---

# AWS ConfigのResourceComplianceを記録除外して一部リソースタイプだけコンプライアンス変更通知を設定してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月31日 14:27
- **URL**: [https://dev.classmethod.jp/articles/config-resourcecompliance-scoped-notification/](https://dev.classmethod.jp/articles/config-resourcecompliance-scoped-notification/)

## 概要

AWS Configの費用高騰を避けたいけど、一部のリソース履歴は残しておきたい…そんな課題はありませんか？今回は、ResourceComplianceの記録を除外しつつ、EventBridgeとの組み合わせで特定のリソースタイプだけ準拠状態を記録する方法をご紹介します。

---

*この記事は自動収集システムによって保存されました。*
