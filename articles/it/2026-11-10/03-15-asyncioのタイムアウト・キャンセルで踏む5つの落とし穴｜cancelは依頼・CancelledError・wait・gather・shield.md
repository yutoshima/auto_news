---
title: "asyncioのタイムアウト・キャンセルで踏む5つの落とし穴｜cancelは依頼・CancelledError・wait・gather・shield"
source: "Qiita (Python)"
category: "it"
published: 2026-11-10T03:15:24
url: https://qiita.com/cauchye_asia/items/a1f2de813c7ce10bcb3f
---

# asyncioのタイムアウト・キャンセルで踏む5つの落とし穴｜cancelは依頼・CancelledError・wait・gather・shield

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年11月10日 03:15
- **URL**: [https://qiita.com/cauchye_asia/items/a1f2de813c7ce10bcb3f](https://qiita.com/cauchye_asia/items/a1f2de813c7ce10bcb3f)

## 概要

TL;DR

Task.cancel() は「キャンセルの依頼」で、返った時点では終わっていません。await で完了を回収し、後始末は finally に書きます。

CancelledError は Exception ではなく BaseException です。明...

---

*この記事は自動収集システムによって保存されました。*
