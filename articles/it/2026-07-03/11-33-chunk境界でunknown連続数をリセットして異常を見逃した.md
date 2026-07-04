---
title: "chunk境界でunknown連続数をリセットして異常を見逃した"
source: "Qiita (JavaScript)"
category: "it"
published: 2026-07-03T11:33:12
url: https://qiita.com/harnesswinner/items/68078a55d246ab05f18e
---

# chunk境界でunknown連続数をリセットして異常を見逃した

## メタデータ

- **情報源**: Qiita (JavaScript)
- **カテゴリ**: it
- **公開日時**: 2026年07月03日 11:33
- **URL**: [https://qiita.com/harnesswinner/items/68078a55d246ab05f18e](https://qiita.com/harnesswinner/items/68078a55d246ab05f18e)

## 概要

TL;DR
バックグラウンド処理を8件ずつのchunkに分けるとき、unknownStreak をchunk内のローカル変数だけにすると、chunk境界で連続数が0に戻る。3件連続 unknown を検知したいなら、chunkの戻り値として連続数を返し、次chunkの i...

---

*この記事は自動収集システムによって保存されました。*
