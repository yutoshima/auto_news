---
title: "【TypeScript】値・型・名前空間の「三重定義」でReactコンポーネントをより柔軟に設計する"
source: "Zenn"
category: "it"
published: 2026-05-15T09:39:14
url: https://zenn.dev/bmth/articles/ts-companion-object
---

# 【TypeScript】値・型・名前空間の「三重定義」でReactコンポーネントをより柔軟に設計する

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年05月15日 09:39
- **URL**: [https://zenn.dev/bmth/articles/ts-companion-object](https://zenn.dev/bmth/articles/ts-companion-object)

## 概要

以下を自然な日本語に翻訳します。

はじめに
TypeScriptにおける、コンパニオンオブジェクトを知っていますか？

export type Rectangle = {
  height: number;
  width: number;
};
 
export const Rectangle = {
  from(height: number, width: number): Rectangle {
    return {
      height,
      width,
    };
  },
};

// Rectangleという宣言が型と値の両方で使える！
const rectangle: Recta...

---

*この記事は自動収集システムによって保存されました。*
