---
title: "GitHub ActionsのSHAピン留めを設定で強制する。何が止まるか、lockfileならタグのまま通せるかを試す"
source: "DevelopersIO"
category: "it"
published: 2026-11-02T13:20:23
url: https://dev.classmethod.jp/articles/github-actions-require-sha-pinning/
---

# GitHub ActionsのSHAピン留めを設定で強制する。何が止まるか、lockfileならタグのまま通せるかを試す

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月02日 13:20
- **URL**: [https://dev.classmethod.jp/articles/github-actions-require-sha-pinning/](https://dev.classmethod.jp/articles/github-actions-require-sha-pinning/)

## 概要

GitHub ActionsのSHAピン留めは設定で強制できます。タグ参照のほか、composite actionの中のタグ参照でも止まりました。GAになったworkflow lockfileならタグのまま通ることを確かめ、フルSHAへの書き換えとの使い分けを整理します。

---

*この記事は自動収集システムによって保存されました。*
