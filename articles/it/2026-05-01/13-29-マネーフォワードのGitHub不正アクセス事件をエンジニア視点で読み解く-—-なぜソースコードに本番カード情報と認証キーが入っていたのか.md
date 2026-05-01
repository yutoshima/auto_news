---
title: "マネーフォワードのGitHub不正アクセス事件をエンジニア視点で読み解く — なぜソースコードに本番カード情報と認証キーが入っていたのか"
source: "Zenn"
category: "it"
published: 2026-05-01T13:29:45
url: https://zenn.dev/awesome_kou/articles/moneyforward-github-source-leak
---

# マネーフォワードのGitHub不正アクセス事件をエンジニア視点で読み解く — なぜソースコードに本番カード情報と認証キーが入っていたのか

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月01日 13:29
- **URL**: [https://zenn.dev/awesome_kou/articles/moneyforward-github-source-leak](https://zenn.dev/awesome_kou/articles/moneyforward-github-source-leak)

## 概要

はじめに
2026 年 5 月 1 日、マネーフォワードが「GitHub への不正アクセス発生に関するお知らせとお詫び（第一報）」を公表しました。GitHub の認証情報が漏えいし、第三者によりリポジトリがコピーされ、ソースコードと一部の個人情報が流出した可能性があるという内容です。同時に、銀行口座連携機能を一時停止する措置もとられました。
この事案は、エンジニア視点で見ると「仕方ない部分」と「明らかにアウトな部分」がはっきり分かれる、教科書のような事例になっています。GitHub 認証情報の漏えい自体は、正直に言ってどの会社でも起こり得ます。一方で、流出したとされる中身に 本番カー...

---

*この記事は自動収集システムによって保存されました。*
