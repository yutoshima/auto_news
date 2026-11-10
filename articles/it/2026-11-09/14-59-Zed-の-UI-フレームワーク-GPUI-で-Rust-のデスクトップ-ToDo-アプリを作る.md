---
title: "Zed の UI フレームワーク GPUI で Rust のデスクトップ ToDo アプリを作る"
source: "はてブ テクノロジー"
category: "it"
published: 2026-11-09T14:59:53
url: https://azukiazusa.dev/blog/gpui-todo-app/
---

# Zed の UI フレームワーク GPUI で Rust のデスクトップ ToDo アプリを作る

## メタデータ

- **情報源**: はてブ テクノロジー
- **カテゴリ**: it
- **公開日時**: 2026年11月09日 14:59
- **URL**: [https://azukiazusa.dev/blog/gpui-todo-app/](https://azukiazusa.dev/blog/gpui-todo-app/)

## 概要

gpui_kit::{prelude::*, *} を使用する。 TodoApp 構造体 { title: SharedString, } を実装する。 impl Render for TodoApp { fn render(&mut self, _window: &mut Window, _cx: &mut Context) -> impl IntoElement { div() .flex() .flex_col() .size_full() .p_4() .bg(rgb(0xffffff)) .text_color(rgb(0x111827)) .child(div().text_...

---

*この記事は自動収集システムによって保存されました。*
