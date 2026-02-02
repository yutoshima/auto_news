---
title: "Reactで「チェックしてるのにエラーが出ない」原因を特定して解決した話"
source: "Qiita (React)"
category: "it"
published: 2026-02-02T10:46:53
url: https://qiita.com/jota9613/items/c4bd4fe23ab0eb8be290
---

# Reactで「チェックしてるのにエラーが出ない」原因を特定して解決した話

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年02月02日 10:46
- **URL**: [https://qiita.com/jota9613/items/c4bd4fe23ab0eb8be290](https://qiita.com/jota9613/items/c4bd4fe23ab0eb8be290)

## 概要

はじめに
Reactで「チェックしてるのにエラーが出ない」原因は
*|| の評価の理解不足 でした。

問題
||の意味を理解していなかった

解決方法
||の意味を理解すること
どれか1つでも true なら、全体が trueになる
if (time === "" ||...

---

*この記事は自動収集システムによって保存されました。*
