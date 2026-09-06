---
title: "[OpenTelemetry] Go のコンパイル時計装において、ctx 伝搬なしで span を紐づける仕組みについて調べた"
source: "Zenn"
category: "it"
published: 2026-09-05T05:20:31
url: https://zenn.dev/ntk221/articles/34cbb95272720f
---

# [OpenTelemetry] Go のコンパイル時計装において、ctx 伝搬なしで span を紐づける仕組みについて調べた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月05日 05:20
- **URL**: [https://zenn.dev/ntk221/articles/34cbb95272720f](https://zenn.dev/ntk221/articles/34cbb95272720f)

## 概要

Go の OpenTelemetry コンパイル時計装(opentelemetry-go-compile-instrumentation の otelc)について調べていると、context.Context を伝搬していなくても span の親子を繋げられる仕組みが入っていることがわかりました。これは GLS(goroutine-local storage) と呼ばれる仕組みです。
Go では span の親子関係を ctx で運ぶのが API の規約なので、ctx を引き回していないコードにそのまま計装を入れても span 同士は繋がりません。GLS はこの隙間を埋めるもので、ctx ...

---

*この記事は自動収集システムによって保存されました。*
