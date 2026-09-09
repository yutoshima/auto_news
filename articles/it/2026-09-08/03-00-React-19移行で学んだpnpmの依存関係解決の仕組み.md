---
title: "React 19移行で学んだpnpmの依存関係解決の仕組み"
source: "Zenn"
category: "it"
published: 2026-09-08T03:00:05
url: https://zenn.dev/yamatechi/articles/vite-monorepo-react-dedupe
---

# React 19移行で学んだpnpmの依存関係解決の仕組み

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月08日 03:00
- **URL**: [https://zenn.dev/yamatechi/articles/vite-monorepo-react-dedupe](https://zenn.dev/yamatechi/articles/vite-monorepo-react-dedupe)

## 概要

こんにちは、Dress Code でプロダクトエンジニアをしているてちです！
少し前にアプリケーションで利用しているReactについて、React18からReact19への移行を行いました。
今回は移行で遭遇した不具合について、調査をしていく中で多くの学びがあったので記事にしてみました。
!
自分なりに調査した内容を書いてますが気になる点あればお気軽にご指摘ください...！


 React19移行で見つかった謎の不具合
pnpm workspaceとViteを使うモノレポで、複数あるReactアプリケーションの一つをReact19に更新しました。他のアプリはReact18のままだったた...

---

*この記事は自動収集システムによって保存されました。*
