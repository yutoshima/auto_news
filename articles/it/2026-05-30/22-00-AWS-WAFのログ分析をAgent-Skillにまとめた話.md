---
title: "AWS WAFのログ分析をAgent Skillにまとめた話"
source: "Zenn"
category: "it"
published: 2026-05-30T22:00:05
url: https://zenn.dev/yamadatt/articles/20260531-aws-waf-log-analysis-claude-skill
---

# AWS WAFのログ分析をAgent Skillにまとめた話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月30日 22:00
- **URL**: [https://zenn.dev/yamadatt/articles/20260531-aws-waf-log-analysis-claude-skill](https://zenn.dev/yamadatt/articles/20260531-aws-waf-log-analysis-claude-skill)

## 概要

はじめに
ALBのアクセスログを眺めていると、/.env や /wp-login.php、/vendor/phpunit/...eval-stdin.php といった、どう見ても正規アクセスではないリクエストが大量に流れているのが見えてきます。
そこで、L7のフィルタが無いALBに対してAWS WAFを導入することにしました。しかし、WAFは「入れたら終わり」ではありません。
AWS WAFの定石は、次の3ステップです。

COUNTモードで導入する
1〜2週間メトリクスとログを観察して誤検知をチューニングする
BLOCKに切り替える

ところがこの「ログを観察する」工程が地味に重い...

---

*この記事は自動収集システムによって保存されました。*
