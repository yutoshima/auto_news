---
title: "ArkorでNext.jsのPPRの届き方をレスポンスから確かめてみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-23T01:51:09
url: https://dev.classmethod.jp/articles/hasuto-arkor-ppr-shell-streaming/
---

# ArkorでNext.jsのPPRの届き方をレスポンスから確かめてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月23日 01:51
- **URL**: [https://dev.classmethod.jp/articles/hasuto-arkor-ppr-shell-streaming/](https://dev.classmethod.jp/articles/hasuto-arkor-ppr-shell-streaming/)

## 概要

先日の jsconf で Arkor を教えてもらったので、触ってみました。わざと3秒待つページをデプロイし、Next.jsのPPRでstatic shellと動的な部分がどの順番で届くのかを、レスポンスの到着時刻、x-arkor-edgeヘッダー、管理画面のBuild outputから確かめています。

---

*この記事は自動収集システムによって保存されました。*
