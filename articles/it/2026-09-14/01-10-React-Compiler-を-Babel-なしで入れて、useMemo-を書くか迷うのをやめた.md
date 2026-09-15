---
title: "React Compiler を Babel なしで入れて、useMemo を書くか迷うのをやめた"
source: "Zenn"
category: "it"
published: 2026-09-14T01:10:32
url: https://zenn.dev/hacobu/articles/2f58be1f62bcf8
---

# React Compiler を Babel なしで入れて、useMemo を書くか迷うのをやめた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月14日 01:10
- **URL**: [https://zenn.dev/hacobu/articles/2f58be1f62bcf8](https://zenn.dev/hacobu/articles/2f58be1f62bcf8)

## 概要

こんにちは。株式会社 Hacobu でフロントエンドエンジニアをしている cho です。
最近、新規プロジェクトを立ち上げています。構成は Vite 8 + React 19.2 + Mantine 9、TanStack Router / Table / Form。一覧と入力フォームが中心で、データもまだモックの段階です。実装の多くは AI に書かせています。
ゼロから作れるので React 19 + Vite 8 で始めましたが、React Compiler の導入だけは見送っていました。Vite 8 で公式の React Compiler を使うには Babel を追加する必要があり...

---

*この記事は自動収集システムによって保存されました。*
