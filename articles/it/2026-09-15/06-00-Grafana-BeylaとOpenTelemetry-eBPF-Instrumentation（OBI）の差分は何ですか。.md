---
title: "Grafana BeylaとOpenTelemetry eBPF Instrumentation（OBI）の差分は何ですか。"
source: "Zenn"
category: "it"
published: 2026-09-15T06:00:04
url: https://zenn.dev/ymotongpoo/articles/20260916-beyla-obi-diff
---

# Grafana BeylaとOpenTelemetry eBPF Instrumentation（OBI）の差分は何ですか。

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月15日 06:00
- **URL**: [https://zenn.dev/ymotongpoo/articles/20260916-beyla-obi-diff](https://zenn.dev/ymotongpoo/articles/20260916-beyla-obi-diff)

## 概要

!
検証環境

ホスト: Ubuntu、カーネル7.0.0-31-generic、/sys/kernel/btf/vmlinux あり
計装対象: nginx:1.27-alpine（ポート80をホストへ公開）
エージェント: otel/ebpf-instrument:v0.13.0（2026-09-04リリース）、grafana/beyla:3.35.0（2026-09-09リリース、OBIサブモジュールは 861d907）
起動方法: docker run --privileged --pid=host --network=host、Prometheusエンドポイントを curl で...

---

*この記事は自動収集システムによって保存されました。*
