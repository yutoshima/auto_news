---
title: "普段使いのWindows PCでNodeのサーバーを常駐させて踏んだ罠"
source: "Zenn"
category: "it"
published: 2026-10-19T11:13:05
url: https://zenn.dev/matasuke_t/articles/bf784b79b29e86
---

# 普段使いのWindows PCでNodeのサーバーを常駐させて踏んだ罠

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月19日 11:13
- **URL**: [https://zenn.dev/matasuke_t/articles/bf784b79b29e86](https://zenn.dev/matasuke_t/articles/bf784b79b29e86)

## 概要

業務用のツールを、専用サーバーではなく普段使っている Windows PC で24時間動かしています。Node.js のバックエンドと、Vite の開発サーバーと、Puppeteer で動かすブラウザが10個ほど。
作ったものが動くかより、「動き続けるか」のほうで何度も詰まったので、そのとき分かったことを書いておきます。

 「起動時」トリガーが一度も発火していなかった
サーバーが35時間止まっていて、原因を調べたらタスクスケジューラのトリガーが「起動時」だけでした。
このPCの最終起動時刻を見たら3週間以上前。
(Get-CimInstance Win32_OperatingSyste...

---

*この記事は自動収集システムによって保存されました。*
