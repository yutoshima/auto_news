---
title: "Amazon Chime SDK で 1 対 1 のビデオ通話を作り、通話後に会議が消えるまでを GetMeeting と CloudTrail で確認してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-25T07:00:09
url: https://dev.classmethod.jp/articles/chime-sdk-meeting-cleanup-getmeeting-cloudtrail/
---

# Amazon Chime SDK で 1 対 1 のビデオ通話を作り、通話後に会議が消えるまでを GetMeeting と CloudTrail で確認してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月25日 07:00
- **URL**: [https://dev.classmethod.jp/articles/chime-sdk-meeting-cleanup-getmeeting-cloudtrail/](https://dev.classmethod.jp/articles/chime-sdk-meeting-cleanup-getmeeting-cloudtrail/)

## 概要

Amazon Chime SDK で 1 対 1 のビデオ通話を作る際、通話終了後に JoinToken で入り直されないようにするには、会議をしっかり終わらせる必要があります。DeleteMeeting を呼ぶ方法と自動終了を待つ方法を、実際に検証してみました。

---

*この記事は自動収集システムによって保存されました。*
