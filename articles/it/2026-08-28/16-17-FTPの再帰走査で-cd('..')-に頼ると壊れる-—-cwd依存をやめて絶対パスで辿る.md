---
title: "FTPの再帰走査で cd('..') に頼ると壊れる — cwd依存をやめて絶対パスで辿る"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-28T16:17:40
url: https://qiita.com/iwadjp/items/1c3ec18982c6d9cc03c6
---

# FTPの再帰走査で cd('..') に頼ると壊れる — cwd依存をやめて絶対パスで辿る

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月28日 16:17
- **URL**: [https://qiita.com/iwadjp/items/1c3ec18982c6d9cc03c6](https://qiita.com/iwadjp/items/1c3ec18982c6d9cc03c6)

## 概要

1. 症状
Node.jsでFTPサーバ上のディレクトリを再帰的に走査するコードを書いたことがあるだろうか。多くの場合、最初に書くのはこういう形になる。
async function scan(dir) {
  await client.cd(dir);

  for (...

---

*この記事は自動収集システムによって保存されました。*
