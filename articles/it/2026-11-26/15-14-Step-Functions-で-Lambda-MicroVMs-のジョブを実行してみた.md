---
title: "Step Functions で Lambda MicroVMs のジョブを実行してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-26T15:14:27
url: https://dev.classmethod.jp/articles/step-functions-lambda-microvms-orchestration/
---

# Step Functions で Lambda MicroVMs のジョブを実行してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月26日 15:14
- **URL**: [https://dev.classmethod.jp/articles/step-functions-lambda-microvms-orchestration/](https://dev.classmethod.jp/articles/step-functions-lambda-microvms-orchestration/)

## 概要

MicroVM の起動、ジョブの実行、終了を、Step Functions のステートマシン（SDK 統合と JSONata）で組めました。同じ MicroVM に送った2つのジョブはファイルとメモリを共有できました。ARM と x86 の MicroVM を並列に動かして docker build も実行できました。

---

*この記事は自動収集システムによって保存されました。*
