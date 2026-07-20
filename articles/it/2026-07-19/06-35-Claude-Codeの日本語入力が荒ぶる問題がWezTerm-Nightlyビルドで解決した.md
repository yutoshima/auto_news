---
title: "Claude Codeの日本語入力が荒ぶる問題がWezTerm Nightlyビルドで解決した"
source: "Zenn"
category: "it"
published: 2026-07-19T06:35:08
url: https://zenn.dev/nuresen/articles/claude-code-ime-wezterm
---

# Claude Codeの日本語入力が荒ぶる問題がWezTerm Nightlyビルドで解決した

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月19日 06:35
- **URL**: [https://zenn.dev/nuresen/articles/claude-code-ime-wezterm](https://zenn.dev/nuresen/articles/claude-code-ime-wezterm)

## 概要

TL;DR

WSL2 + WezTerm で Claude Code の TUI に日本語入力すると表示が乱れる（変換候補が変な場所に出る、IME 切り替え直後に荒ぶる）
原因は WezTerm 安定版（20240203）が2年以上更新されておらず、IME まわりの修正が nightly にしか入っていないこと

nightly ビルドに更新するだけで解決。ime_preedit_rendering = "System" などの設定変更は不要だった


 環境



項目
内容




OS
Windows 11 + WSL2 (Ubuntu)


ターミナル
WezTerm（Wi...

---

*この記事は自動収集システムによって保存されました。*
