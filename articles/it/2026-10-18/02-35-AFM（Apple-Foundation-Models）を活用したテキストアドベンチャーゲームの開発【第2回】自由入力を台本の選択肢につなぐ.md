---
title: "AFM（Apple Foundation Models）を活用したテキストアドベンチャーゲームの開発【第2回】自由入力を台本の選択肢につなぐ"
source: "Zenn"
category: "it"
published: 2026-10-18T02:35:56
url: https://zenn.dev/gritchbreed/articles/ced633f449178f
---

# AFM（Apple Foundation Models）を活用したテキストアドベンチャーゲームの開発【第2回】自由入力を台本の選択肢につなぐ

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月18日 02:35
- **URL**: [https://zenn.dev/gritchbreed/articles/ced633f449178f](https://zenn.dev/gritchbreed/articles/ced633f449178f)

## 概要

はじめに
※この記事は、筆者のQiitaアカウントからの転載（マルチポスト）です。
Apple Foundation Models（以下AFM）のオンデバイスモデルを使って、自由入力のテキストアドベンチャーゲームを開発しています。
第1回では、デモ「血の池の夜」と、AFMに入力の解釈・自由会話・記憶の取り出しを任せ、物語の進行は台本とルールエンジンで制御する全体設計を紹介しました。
今回は、その中の「入力の解釈」を扱います。プレイヤーの自由な言葉を、ゲームが処理できる話題や移動に変換する部分です。
第1回の全体図に、今回扱う範囲を赤い太枠で示しました。台本に書いた話題から候補を作り、...

---

*この記事は自動収集システムによって保存されました。*
