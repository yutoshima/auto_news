---
title: "miseの1Passwordの環境変数読み込みのたびに数秒待たされるのを、fnoxのdaemonで解消してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-30T11:10:28
url: https://dev.classmethod.jp/articles/mise-secret-cache-fnox-daemon/
---

# miseの1Passwordの環境変数読み込みのたびに数秒待たされるのを、fnoxのdaemonで解消してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月30日 11:10
- **URL**: [https://dev.classmethod.jp/articles/mise-secret-cache-fnox-daemon/](https://dev.classmethod.jp/articles/mise-secret-cache-fnox-daemon/)

## 概要

miseの[env]で1Passwordから読み込んでいたトークンが、miseのアップデート後はEnterのたびに読み直されるようになりました。原因を調べて、hook_env.chpwd_onlyとfnoxのdaemonで0.01秒前後まで戻した記録です。

---

*この記事は自動収集システムによって保存されました。*
