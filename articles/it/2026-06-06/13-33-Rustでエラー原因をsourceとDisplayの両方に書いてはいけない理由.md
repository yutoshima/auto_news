---
title: "Rustでエラー原因をsourceとDisplayの両方に書いてはいけない理由"
source: "Zenn"
category: "it"
published: 2026-06-06T13:33:57
url: https://zenn.dev/ultimatile/articles/rust-error-source-display-duplication
---

# Rustでエラー原因をsourceとDisplayの両方に書いてはいけない理由

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月06日 13:33
- **URL**: [https://zenn.dev/ultimatile/articles/rust-error-source-display-duplication](https://zenn.dev/ultimatile/articles/rust-error-source-display-duplication)

## 概要

!

 TL;DR

責務分担: Displayは自エラーの説明。source()は原因へのリンク。reporterは全体の表示。
原因を#[source]/#[from]で露出するなら、同じ原因を#[error("...: {0}")]でDisplayに重ねない。
重ねるとanyhow等のreporterがsource()を辿り、同じ原因が重複表示される。
文脈ありなら#[error("自レイヤの文脈")]+#[source]。文脈なしラッパーなら#[error(transparent)]。

error.to_string()単独なら例外的にありうる。reporter併用ではfoot...

---

*この記事は自動収集システムによって保存されました。*
