---
title: "GPUとゼロスケールに対応したLambda Managed InstancesでLLMを実行する関数を作って動かしたら、コールドスタートに約4分20秒かかった"
source: "DevelopersIO"
category: "it"
published: 2026-11-19T06:38:37
url: https://dev.classmethod.jp/articles/lambda-managed-instances-gpu-vllm-scale-to-zero/
---

# GPUとゼロスケールに対応したLambda Managed InstancesでLLMを実行する関数を作って動かしたら、コールドスタートに約4分20秒かかった

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月19日 06:38
- **URL**: [https://dev.classmethod.jp/articles/lambda-managed-instances-gpu-vllm-scale-to-zero/](https://dev.classmethod.jp/articles/lambda-managed-instances-gpu-vllm-scale-to-zero/)

## 概要

最近相次いで発表されたLambda Managed InstancesのGPU対応とゼロスケール機能。実際にg6e.xlargeでvLLMとQwen3-30B-A3Bを動かし、ゼロスケール状態からのコールドスタートにかかる時間と内訳を測ってみました。

---

*この記事は自動収集システムによって保存されました。*
