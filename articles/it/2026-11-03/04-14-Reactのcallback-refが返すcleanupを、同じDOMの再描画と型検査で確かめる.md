---
title: "Reactのcallback refが返すcleanupを、同じDOMの再描画と型検査で確かめる"
source: "Qiita (React)"
category: "it"
published: 2026-11-03T04:14:59
url: https://qiita.com/hiro123/items/d36e10885b95a6dfee92
---

# Reactのcallback refが返すcleanupを、同じDOMの再描画と型検査で確かめる

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年11月03日 04:14
- **URL**: [https://qiita.com/hiro123/items/d36e10885b95a6dfee92](https://qiita.com/hiro123/items/d36e10885b95a6dfee92)

## 概要

Reactのcallback refは、DOM nodeを受け取るだけでなく、解除時に呼ぶcleanup関数を返せます。React 19で追加されたこの仕組みを、ResizeObserverの登録と解除で確認しました。
見たいのはunmountだけではありません。同じDOM...

---

*この記事は自動収集システムによって保存されました。*
