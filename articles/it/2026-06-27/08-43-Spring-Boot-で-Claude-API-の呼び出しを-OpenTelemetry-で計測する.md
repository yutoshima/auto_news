---
title: "Spring Boot で Claude API の呼び出しを OpenTelemetry で計測する"
source: "Zenn"
category: "it"
published: 2026-06-27T08:43:31
url: https://zenn.dev/propagandist/articles/0004-spring-boot-otel-claude-observability
---

# Spring Boot で Claude API の呼び出しを OpenTelemetry で計測する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月27日 08:43
- **URL**: [https://zenn.dev/propagandist/articles/0004-spring-boot-otel-claude-observability](https://zenn.dev/propagandist/articles/0004-spring-boot-otel-claude-observability)

## 概要

この記事について


対象読者：Spring Boot から Claude API を呼んでいて、そのレイテンシ・トークン・コスト・失敗を可視化したい人／LLM 呼び出しに OpenTelemetry を入れる最小の型を知りたい人

得られること：Spring Boot 3 標準の Micrometer Observation を OpenTelemetry（OTLP）で送り出し、Claude 呼び出しを 1 本の span として計測する方法。さらにトークン数と推定コストをメトリクス化し、ローカルの OTel Collector → Jaeger・Prometheus・Grafan...

---

*この記事は自動収集システムによって保存されました。*
