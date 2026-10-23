---
title: "Rootless DockerとSELinuxを学ぶ【初心者向け】"
source: "Zenn"
category: "it"
published: 2026-10-22T11:50:59
url: https://zenn.dev/nexryai/articles/afb828d7dda6b7
---

# Rootless DockerとSELinuxを学ぶ【初心者向け】

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月22日 11:50
- **URL**: [https://zenn.dev/nexryai/articles/afb828d7dda6b7](https://zenn.dev/nexryai/articles/afb828d7dda6b7)

## 概要

!
この記事の作成にあたって、図の生成、調査、校正に生成AIを使用していますが、本文は人の手で書かれたものです。


 環境

Rocky Linux 10.2


 あらすじ
私の自宅サーバーでは、/var/composeにDocker Composeのファイル一式を格納し、composeユーザーでRootless Dockerを動かしています。
Rocky Linux（というかRHEL）ではデフォルトでrootで動作する常駐プロセスがありますが、これらからのアクセス制限がどんな感じでかかってるのかを調査してSELinuxの基礎を学んだというお話です。

 前提知識
SELinuxは主...

---

*この記事は自動収集システムによって保存されました。*
