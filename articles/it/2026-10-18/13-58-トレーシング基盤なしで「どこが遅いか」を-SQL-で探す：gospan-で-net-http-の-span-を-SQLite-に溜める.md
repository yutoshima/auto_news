---
title: "トレーシング基盤なしで「どこが遅いか」を SQL で探す：gospan で net/http の span を SQLite に溜める"
source: "はてブ テクノロジー"
category: "it"
published: 2026-10-18T13:58:52
url: https://zenn.dev/nonejp/articles/c7dd2859872f9d
---

# トレーシング基盤なしで「どこが遅いか」を SQL で探す：gospan で net/http の span を SQLite に溜める

## メタデータ

- **情報源**: はてブ テクノロジー
- **カテゴリ**: it
- **公開日時**: 2026年10月18日 13:58
- **URL**: [https://zenn.dev/nonejp/articles/c7dd2859872f9d](https://zenn.dev/nonejp/articles/c7dd2859872f9d)

## 概要

はじめに：1つのプロセスが遅いだけなのに、collector まで立てますか？ Go の API サーバーで「たまに 40ms かかるリクエストがある。でもどの処理が原因か分からない」という場面、ありませんか？ ログに経過時間を出すと「遅かった」ことは分かります。ただ、どの子処理が時間を食ったのか、どの入力で遅くなるのかを...

---

*この記事は自動収集システムによって保存されました。*
