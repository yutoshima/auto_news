---
title: "Kiro CLI V3 の 新機能 「Approve for me」 どの様な操作が確認になるか試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-30T14:06:39
url: https://dev.classmethod.jp/articles/kiro-cli-v3-approve-for-me/
---

# Kiro CLI V3 の 新機能 「Approve for me」 どの様な操作が確認になるか試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月30日 14:06
- **URL**: [https://dev.classmethod.jp/articles/kiro-cli-v3-approve-for-me/](https://dev.classmethod.jp/articles/kiro-cli-v3-approve-for-me/)

## 概要

Kiro CLI V3 の Approve for me で、どの操作が承認され、どの操作が確認に回るかを試しました。rm -rf、force push、/tmp への書き込みは確認なしで承認され、スクリプトを sh に渡す操作は確認に回りました。.git や .kiro/hooks への書き込みの確認と、.kiro/settings への書き込みの拒否は、固定規則によるものでした。

---

*この記事は自動収集システムによって保存されました。*
