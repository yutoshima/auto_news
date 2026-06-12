---
title: "Laravel JavaScriptでのデータの受け渡し"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-06-11T23:31:26
url: https://qiita.com/kkkium/items/6dfec2d8d794aa86bda0
---

# Laravel JavaScriptでのデータの受け渡し

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年06月11日 23:31
- **URL**: [https://qiita.com/kkkium/items/6dfec2d8d794aa86bda0](https://qiita.com/kkkium/items/6dfec2d8d794aa86bda0)

## 概要

1. Laravelから連想配列をJSON形式で送る方法
Route::get('/api/user', function () {

    $user = [
        'name' => '田中',
        'age' => 25,
    ];

    ...

---

*この記事は自動収集システムによって保存されました。*
