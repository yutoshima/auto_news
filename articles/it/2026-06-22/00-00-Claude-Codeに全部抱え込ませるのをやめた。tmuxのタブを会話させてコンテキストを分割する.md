---
title: "Claude Codeに全部抱え込ませるのをやめた。tmuxのタブを会話させてコンテキストを分割する"
source: "Zenn"
category: "it"
published: 2026-06-22T00:00:08
url: https://zenn.dev/tokium_dev/articles/tmux-multitab-context-management
---

# Claude Codeに全部抱え込ませるのをやめた。tmuxのタブを会話させてコンテキストを分割する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月22日 00:00
- **URL**: [https://zenn.dev/tokium_dev/articles/tmux-multitab-context-management](https://zenn.dev/tokium_dev/articles/tmux-multitab-context-management)

## 概要

こんにちは、TOKIUMでエンジニアをしている西本です。
早速ですが、Claude Codeを使い込むほど、ひとつの壁にぶつかります。コンテキストです。1つのセッションに実装もレビューも調査も定型業務も全部やらせていると、コンテキストウィンドウがどんどん膨らみます。長くなれば応答の精度は落ちますし、/compactが走ると直前まで握っていた文脈が要約に丸められて、細部が飛びます。「さっき決めた方針、もう覚えてないな」とぼやく、あの感じです。
コンテキスト管理のノウハウ自体は、世の中にもうたくさん出ています。なので目新しい原則の解説というより、自分の環境を紹介がてら、私なりの落とし込み方を...

---

*この記事は自動収集システムによって保存されました。*
