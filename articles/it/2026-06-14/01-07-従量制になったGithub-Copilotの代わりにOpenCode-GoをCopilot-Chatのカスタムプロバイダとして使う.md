---
title: "従量制になったGithub Copilotの代わりにOpenCode GoをCopilot Chatのカスタムプロバイダとして使う"
source: "Zenn"
category: "it"
published: 2026-06-14T01:07:01
url: https://zenn.dev/kusuke/articles/82129236caa5f8
---

# 従量制になったGithub Copilotの代わりにOpenCode GoをCopilot Chatのカスタムプロバイダとして使う

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年06月14日 01:07
- **URL**: [https://zenn.dev/kusuke/articles/82129236caa5f8](https://zenn.dev/kusuke/articles/82129236caa5f8)

## 概要

Github Copilotが2026年6月より、クレジット制というか従量課金モデルに移行してしまいました。企業の経営のためには仕方がないのですが、個人としてはできれば安く定額で使いたい。
定額制で安くといえばOpenCode Goが有名ですが、こちらはVSCodeのチャットインテグレーションが公式対応していません。
そこで今回は、VSCode最新バージョンから利用可能になっていた「Custom Endpoint」を使って$10で定額制のOpenCode Goを使えるようにしてみました。基本設定はこちらの記事を参考に最新バージョンに合わせて調整しました。この記事は100％人間によって書か...

---

*この記事は自動収集システムによって保存されました。*
