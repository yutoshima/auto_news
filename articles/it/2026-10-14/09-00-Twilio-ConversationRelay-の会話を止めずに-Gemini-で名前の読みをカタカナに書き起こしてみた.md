---
title: "Twilio ConversationRelay の会話を止めずに Gemini で名前の読みをカタカナに書き起こしてみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-14T09:00:11
url: https://dev.classmethod.jp/articles/twilio-conversationrelay-name-katakana-gemini/
---

# Twilio ConversationRelay の会話を止めずに Gemini で名前の読みをカタカナに書き起こしてみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月14日 09:00
- **URL**: [https://dev.classmethod.jp/articles/twilio-conversationrelay-name-katakana-gemini/](https://dev.classmethod.jp/articles/twilio-conversationrelay-name-katakana-gemini/)

## 概要

Twilio ConversationRelay の日本語の音声認識では、名前をカタカナで書き起こすといった表記の制御ができません。そこで会話を保ったまま、名前を伺う区間の声だけを Media Streams で受け取り、Gemini でカタカナに書き起こしました。名前の読みをカタカナで取得し、同じ会話へ戻せました。

---

*この記事は自動収集システムによって保存されました。*
