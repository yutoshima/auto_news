---
title: "Amazon Bedrock AgentCoreは、トレースとログを単一のロググループに統合した観測性を提供します。"
source: "AWS What's New"
category: "it"
published: 2026-07-23T17:00:00
url: https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/
---

# Amazon Bedrock AgentCoreは、トレースとログを単一のロググループに統合した観測性を提供します。

## メタデータ

- **情報源**: AWS What's New
- **カテゴリ**: it
- **公開日時**: 2026年07月23日 17:00
- **URL**: [https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/)

## 概要

<p>Amazon Bedrock AgentCoreは現在、エージェントのトレースとプロンプトをエージェントのログと同じロググループに配信し、1つのAmazon CloudWatchロググループでAIエージェントの統合的な観測性を提供します。</p> 
<p>従来、AgentCoreはエージェントのテレメトリを複数の宛先に分散しており、トレーススパンは共有の`aws/spans`ロググループに、プロンプト・入力・出力を含むイベントログはリソース固有の別のロググループに送られていました。つまり、エージェントの呼び出しをデバッグするには検索が必要でした。

---

*この記事は自動収集システムによって保存されました。*
