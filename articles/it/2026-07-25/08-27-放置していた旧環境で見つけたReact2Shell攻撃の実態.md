---
title: "放置していた旧環境で見つけたReact2Shell攻撃の実態"
source: "Zenn"
category: "it"
published: 2026-07-25T08:27:52
url: https://zenn.dev/munenick/articles/b507a9848b6fdd
---

# 放置していた旧環境で見つけたReact2Shell攻撃の実態

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年07月25日 08:27
- **URL**: [https://zenn.dev/munenick/articles/b507a9848b6fdd](https://zenn.dev/munenick/articles/b507a9848b6fdd)

## 概要

はじめに
本記事は以下のミラーです。
https://www.munenick.me/blog/react2shell-attack-in-abandoned-kubernetes/
私は自宅でKubernetesクラスタやゲームサーバー、いくつかのWebアプリケーションを運営しています。普段使う機能は新しいシステムへ移していましたが、旧Kubernetes環境の一部は止めず、インターネットに公開したまま残していました。使わなくなるにつれて、依存パッケージの更新や監視もしなくなっていました。
旧環境には攻撃が繰り返し届き、気づかないうちにハニーポットのような状態になっていました。侵入...

---

*この記事は自動収集システムによって保存されました。*
