---
title: "Windows の Node で fetch のあとに process.exit(0) すると、仕事を終えたあとに終了コード 3221226505 で落ちる回があった。このPCで数えると fetch 3回と4回で20回中20回、5回で1〜5回、8回で0回だった"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-10-14T22:43:50
url: https://qiita.com/AUTOMOS/items/5edccbff9c8f381beba1
---

# Windows の Node で fetch のあとに process.exit(0) すると、仕事を終えたあとに終了コード 3221226505 で落ちる回があった。このPCで数えると fetch 3回と4回で20回中20回、5回で1〜5回、8回で0回だった

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 22:43
- **URL**: [https://qiita.com/AUTOMOS/items/5edccbff9c8f381beba1](https://qiita.com/AUTOMOS/items/5edccbff9c8f381beba1)

## 概要

定期実行している確認用のスクリプトが、表示も処理もすべて正しく終わったあとに、失敗の終了コードを返していました。
Assertion failed: !(handle-&gt;flags &amp; UV_HANDLE_CLOSING), file src\win\async.c, li...

---

*この記事は自動収集システムによって保存されました。*
