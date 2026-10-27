---
title: "Claude Desktop で「このデバイスでは WSL セッションを利用できません」と出たときの原因と対処"
source: "DevelopersIO"
category: "it"
published: 2026-10-26T14:49:18
url: https://dev.classmethod.jp/articles/claude-desktop-disable-wsl-sessions-registry-policy/
---

# Claude Desktop で「このデバイスでは WSL セッションを利用できません」と出たときの原因と対処

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月26日 14:49
- **URL**: [https://dev.classmethod.jp/articles/claude-desktop-disable-wsl-sessions-registry-policy/](https://dev.classmethod.jp/articles/claude-desktop-disable-wsl-sessions-registry-policy/)

## 概要

Claude Desktop のポリシー（レジストリ値）を 1 つでも設定すると、Code タブの WSL セッションがエラーで使えなくなります。disableWslSessions を 0 で追加して、ポリシーの設定を残したままエラーが解消できることを、検証で確かめました。

---

*この記事は自動収集システムによって保存されました。*
