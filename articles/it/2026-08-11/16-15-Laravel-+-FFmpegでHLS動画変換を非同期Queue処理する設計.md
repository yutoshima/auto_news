---
title: "Laravel + FFmpegでHLS動画変換を非同期Queue処理する設計"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-08-11T16:15:10
url: https://qiita.com/ChrisBlank/items/90e2b1fa369393a28013
---

# Laravel + FFmpegでHLS動画変換を非同期Queue処理する設計

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年08月11日 16:15
- **URL**: [https://qiita.com/ChrisBlank/items/90e2b1fa369393a28013](https://qiita.com/ChrisBlank/items/90e2b1fa369393a28013)

## 概要

Webアプリケーションでユーザーから動画を受け取り、HLS形式へ変換する場合、FFmpegをHTTPリクエスト内で直接実行するのは避けたいところです。
例えば、次のような処理です。
Upload
  ↓
FFmpeg
  ↓
HLS生成
  ↓
Response

数秒で終...

---

*この記事は自動収集システムによって保存されました。*
