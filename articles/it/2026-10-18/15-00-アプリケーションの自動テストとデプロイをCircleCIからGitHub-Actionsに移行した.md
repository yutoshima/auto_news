---
title: "アプリケーションの自動テストとデプロイをCircleCIからGitHub Actionsに移行した"
source: "Zenn"
category: "it"
published: 2026-10-18T15:00:05
url: https://zenn.dev/tsukulink/articles/fea41a6e4113cf
---

# アプリケーションの自動テストとデプロイをCircleCIからGitHub Actionsに移行した

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月18日 15:00
- **URL**: [https://zenn.dev/tsukulink/articles/fea41a6e4113cf](https://zenn.dev/tsukulink/articles/fea41a6e4113cf)

## 概要

こんにちは！ツクリンクでエンジニアをしている oieioi です。
ツクリンクは開発用の CI を CircleCI から GitHub Actions に移行しました。移行してから半年間障害なく運用できているので、移行時にしたことを書いてみます。

 移行したもの
移行対象は3つあった。

プルリクエストに対する継続的なテスト
検証環境(AWS)へのデプロイ

インフラのデプロイ
アプリケーションのデプロイ


商用環境(AWS)へのデプロイ

インフラのデプロイ
アプリケーションのデプロイ



デプロイは terraform と ecspresso でコード化してあった。

 移行...

---

*この記事は自動収集システムによって保存されました。*
