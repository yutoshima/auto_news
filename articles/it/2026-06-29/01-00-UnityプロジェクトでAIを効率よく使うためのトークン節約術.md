---
title: "UnityプロジェクトでAIを効率よく使うためのトークン節約術"
source: "Zenn"
category: "it"
published: 2026-06-29T01:00:09
url: https://zenn.dev/gamedev_toollab/articles/a7364d37455a50
---

# UnityプロジェクトでAIを効率よく使うためのトークン節約術

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月29日 01:00
- **URL**: [https://zenn.dev/gamedev_toollab/articles/a7364d37455a50](https://zenn.dev/gamedev_toollab/articles/a7364d37455a50)

## 概要

はじめに
開発中、または運用中のUnityプロジェクトでAIコーディングエージェントを使うと、調査・実装・レビューの速度はかなり上がります。
一方で、プロジェクトが大きくなるほど次の問題が起きやすくなります。

関係ないフォルダまで読みに行く

Library/ や Temp/ などの生成物を読もうとする
Scene / Prefab / ScriptableObject の巨大YAMLを丸ごと読む
Addressablesの生成物やログを読み込んでトークンを消費する
毎回同じプロジェクト説明をチャットで繰り返す

AGENTS.md / CLAUDE.md に書きすぎて、逆に守られ...

---

*この記事は自動収集システムによって保存されました。*
