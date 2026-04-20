---
title: "環境が汚れるのが嫌なのでPodmanコンテナの中でSteamを動かした"
source: "Zenn"
category: "it"
published: 2026-04-19T23:40:05
url: https://zenn.dev/headwaters/articles/c4a62943ec50aa
---

# 環境が汚れるのが嫌なのでPodmanコンテナの中でSteamを動かした

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月19日 23:40
- **URL**: [https://zenn.dev/headwaters/articles/c4a62943ec50aa](https://zenn.dev/headwaters/articles/c4a62943ec50aa)

## 概要

はじめに
Linuxでゲームをするとき、Steamをインストールすると32bitライブラリやら依存パッケージやらがドッと入ってきて、システムが少しずつ汚れていく。
「ゲームは遊びたい、でも環境は汚したくない」
そんなわがままを叶えるために、rootless Podmanコンテナの中でSteamを動かす仕組みを作った。
コンテナを消せばSteamの痕跡はゼロ。データも1つのディレクトリに閉じ込めてあるので、フォルダごと消せば完全にクリーンな状態に戻る。
https://github.com/yuma-seno/podman-steam

 セットアップは2コマンド
chmod +x r...

---

*この記事は自動収集システムによって保存されました。*
