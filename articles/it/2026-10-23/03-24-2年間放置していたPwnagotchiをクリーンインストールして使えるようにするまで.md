---
title: "2年間放置していたPwnagotchiをクリーンインストールして使えるようにするまで"
source: "Zenn"
category: "it"
published: 2026-10-23T03:24:22
url: https://zenn.dev/kuroikotech/articles/pwnagotchi-zero2w-clean-install
---

# 2年間放置していたPwnagotchiをクリーンインストールして使えるようにするまで

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月23日 03:24
- **URL**: [https://zenn.dev/kuroikotech/articles/pwnagotchi-zero2w-clean-install](https://zenn.dev/kuroikotech/articles/pwnagotchi-zero2w-clean-install)

## 概要

はじめに
2年ほど放置していたPwnagotchiを、久しぶりに動かすことにした。
古い環境をそのまま直すのではなく、microSDを焼き直してクリーンインストールする。画面を動かして、SSHで入れて、バッテリーで持ち運べる状態に戻すのが今回の目標。
イメージを書き込めばすぐ終わるかと思ったら、USB接続でかなりハマった。最終的にはディスプレイとPiSugarの認識、SSHの鍵認証、PCからのインターネット共有までできたので、その記録を残す。
!
Pwnagotchiは無線ネットワークのセキュリティ検証に使うツール。検証は自分が管理するネットワークか、明確な許可を得た環境で行う。
今...

---

*この記事は自動収集システムによって保存されました。*
