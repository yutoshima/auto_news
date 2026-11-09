---
title: "Amazon Chime SDK の通話に同じ会員が 2 台目の端末から入ると、1 台目がどうなるかを参加者の作り方ごとに確認してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-08T21:00:09
url: https://dev.classmethod.jp/articles/chime-sdk-same-member-second-device-attendee-patterns/
---

# Amazon Chime SDK の通話に同じ会員が 2 台目の端末から入ると、1 台目がどうなるかを参加者の作り方ごとに確認してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月08日 21:00
- **URL**: [https://dev.classmethod.jp/articles/chime-sdk-same-member-second-device-attendee-patterns/](https://dev.classmethod.jp/articles/chime-sdk-same-member-second-device-attendee-patterns/)

## 概要

Amazon Chime SDKで1対1のビデオ通話中に複数端末から接続する場合、参加者の作り方によって挙動が大きく変わります。同じExternalUserIdで作る場合、端末ごとに変える場合、削除してから作り直す場合の3通りを実際に試し、それぞれの端末やサーバー側でどのような動作が起こるかを確認しました。

---

*この記事は自動収集システムによって保存されました。*
