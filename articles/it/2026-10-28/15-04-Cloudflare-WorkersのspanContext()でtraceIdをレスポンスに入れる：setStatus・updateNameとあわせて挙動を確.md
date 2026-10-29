---
title: "Cloudflare WorkersのspanContext()でtraceIdをレスポンスに入れる：setStatus・updateNameとあわせて挙動を確かめる"
source: "DevelopersIO"
category: "it"
published: 2026-10-28T15:04:32
url: https://dev.classmethod.jp/articles/cloudflare-workers-span-context-status/
---

# Cloudflare WorkersのspanContext()でtraceIdをレスポンスに入れる：setStatus・updateNameとあわせて挙動を確かめる

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月28日 15:04
- **URL**: [https://dev.classmethod.jp/articles/cloudflare-workers-span-context-status/](https://dev.classmethod.jp/articles/cloudflare-workers-span-context-status/)

## 概要

Workersのカスタムspanに追加されたspanContext()、setStatus()、updateName()を試し、traceIdがダッシュボードのトレースと一致するか、名前とstatusが本番とLocal Explorerでどう見えるかを確かめました。

---

*この記事は自動収集システムによって保存されました。*
