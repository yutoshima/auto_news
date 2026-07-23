---
title: "Souther - ドメインモデルをスラスラ書けることを追い求めた最果てのJVM言語"
source: "Zenn"
category: "it"
published: 2026-07-22T09:36:32
url: https://zenn.dev/kawasima/articles/souther-essentials
---

# Souther - ドメインモデルをスラスラ書けることを追い求めた最果てのJVM言語

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月22日 09:36
- **URL**: [https://zenn.dev/kawasima/articles/souther-essentials](https://zenn.dev/kawasima/articles/souther-essentials)

## 概要

Javaでドメインモデルを素直に表そうとすると、型が増えます。従業員IDと文字列を分け、金額と整数を分け、申請の状態ごとに別の型を用意する。値の検証や業務上の却下も型と戻り値で表し、現在時刻やデータベースアクセスは外から注入する。業務上の違いをコードの構造へ反映するほど、コンストラクタ、アクセサ、変換処理などの実装も増えていきます。
問題は、それらが規約にとどまることです。検証を通らない構築経路を残すことも、業務上の却下を例外で返すことも、業務ロジックから直接データベースへ触ることもできます。設計を守るには、実装者が毎回同じ判断をしなければなりません。

Souther は、業務上の概念...

---

*この記事は自動収集システムによって保存されました。*
