---
title: "ProgateのレッスンにChromeの開発者ツールを丸ごと埋め込んだ話"
source: "Zenn"
category: "it"
published: 2026-06-18T08:52:44
url: https://zenn.dev/progate/articles/progate-embed-devtools
---

# ProgateのレッスンにChromeの開発者ツールを丸ごと埋め込んだ話

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月18日 08:52
- **URL**: [https://zenn.dev/progate/articles/progate-embed-devtools](https://zenn.dev/progate/articles/progate-embed-devtools)

## 概要

はじめに
HTML・CSSを学んでいると、「marginがなんで効かないんだろう？」「この要素ってどういう構造になってるんだろう？」と気になる場面がよくあります。普段の開発ならChromeのデベロッパーツールをパッと開いて要素を検証すればいいのですが、学習サービスのプレビューはiframeの中にあることが多く、普通にデベロッパーツールを開くと学習に関係のないサービス本体の要素やコンソールまで表示されてしまうという問題があります。
しかも、検証するにはブラウザー標準のデベロッパーツールを開くしかなかったので、その分だけ学習画面が圧迫されてしまうのも地味につらいところでした。こんな感じで...

---

*この記事は自動収集システムによって保存されました。*
