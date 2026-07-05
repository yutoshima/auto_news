---
title: "自ホストLLMインフラのRCEラッシュ（2026年6月）：transformersのconfig.json実行とLiteLLM×Starlette連鎖（CVSS 10・CISA KEV入り）を今すぐ塞ぐ"
source: "Qiita (Python)"
category: "it"
published: 2026-07-05T22:39:37
url: https://qiita.com/YushiYamamoto/items/8ce1f18026aaff8d9189
---

# 自ホストLLMインフラのRCEラッシュ（2026年6月）：transformersのconfig.json実行とLiteLLM×Starlette連鎖（CVSS 10・CISA KEV入り）を今すぐ塞ぐ

## メタデータ

- **情報源**: Qiita (Python)
- **カテゴリ**: it
- **公開日時**: 2026年07月05日 22:39
- **URL**: [https://qiita.com/YushiYamamoto/items/8ce1f18026aaff8d9189](https://qiita.com/YushiYamamoto/items/8ce1f18026aaff8d9189)

## 概要

2026年5〜6月にかけて、自分でホストするLLM/AIインフラの「供給網」を狙った深刻なRCE（リモートコード実行）が立て続けに表面化した。
モデルを読み込むだけで発火するHugging Face transformers の欠陥、AIゲートウェイ LiteLLM のコ...

---

*この記事は自動収集システムによって保存されました。*
