---
title: "[アップデート] Amazon ECS の GPU 共有でコンテナごとのメモリ・演算の上限が守られるか試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-10-29T03:54:27
url: https://dev.classmethod.jp/articles/amazon-ecs-gpu-sharing-nvidia-mps/
---

# [アップデート] Amazon ECS の GPU 共有でコンテナごとのメモリ・演算の上限が守られるか試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月29日 03:54
- **URL**: [https://dev.classmethod.jp/articles/amazon-ecs-gpu-sharing-nvidia-mps/](https://dev.classmethod.jp/articles/amazon-ecs-gpu-sharing-nvidia-mps/)

## 概要

Amazon ECS の GPU 共有（NVIDIA MPS）を検証しました。メモリと演算の上限は指定通りに守られ、演算の上限の合計が 100% 以内なら性能も互いに影響しませんでした。一方で、コンテナ内で環境変数を書き換えると上限を外せることも分かりました。

---

*この記事は自動収集システムによって保存されました。*
