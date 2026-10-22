---
title: "PlaywrightのTrace Viewerで、失敗したE2Eテストの原因を調べる"
source: "DevelopersIO"
category: "it"
published: 2026-10-21T02:15:51
url: https://dev.classmethod.jp/articles/playwright-trace-viewer-debugging/
---

# PlaywrightのTrace Viewerで、失敗したE2Eテストの原因を調べる

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月21日 02:15
- **URL**: [https://dev.classmethod.jp/articles/playwright-trace-viewer-debugging/](https://dev.classmethod.jp/articles/playwright-trace-viewer-debugging/)

## 概要

PlaywrightのE2Eテストがタイムアウトしたとき、待ち時間を延ばす前にTrace Viewerで失敗時の状態を調べます。APIが500を返すサンプルを使い、失敗したexpect、画面の状態、通信の応答を順に確認し、修正後の成功まで追いました。

---

*この記事は自動収集システムによって保存されました。*
