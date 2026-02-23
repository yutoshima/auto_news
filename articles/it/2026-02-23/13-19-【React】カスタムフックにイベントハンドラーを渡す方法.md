---
title: "【React】カスタムフックにイベントハンドラーを渡す方法"
source: "Qiita (React)"
category: "it"
published: 2026-02-23T13:19:00
url: https://qiita.com/P-man_Brown/items/030dfb919d99aee23e56
---

# 【React】カスタムフックにイベントハンドラーを渡す方法

## メタデータ

- **情報源**: Qiita (React)
- **カテゴリ**: it
- **公開日時**: 2026年02月23日 13:19
- **URL**: [https://qiita.com/P-man_Brown/items/030dfb919d99aee23e56](https://qiita.com/P-man_Brown/items/030dfb919d99aee23e56)

## 概要

実装方法
onReceiveMessage をオプションとして受け取るようにします。
以下のようにuseEffectEvent を使うと、イベントハンドラーを依存配列から除外できます。
コンポーネントが再レンダリングされても不必要な再接続が発生しなくなります。
impor...

---

*この記事は自動収集システムによって保存されました。*
