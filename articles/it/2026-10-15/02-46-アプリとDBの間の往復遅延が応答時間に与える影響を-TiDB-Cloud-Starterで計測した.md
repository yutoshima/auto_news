---
title: "アプリとDBの間の往復遅延が応答時間に与える影響を TiDB Cloud Starterで計測した"
source: "DevelopersIO"
category: "it"
published: 2026-10-15T02:46:08
url: https://dev.classmethod.jp/articles/tidb-cloud-network-latency-app-response/
---

# アプリとDBの間の往復遅延が応答時間に与える影響を TiDB Cloud Starterで計測した

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年10月15日 02:46
- **URL**: [https://dev.classmethod.jp/articles/tidb-cloud-network-latency-app-response/](https://dev.classmethod.jp/articles/tidb-cloud-network-latency-app-response/)

## 概要

アプリと TiDB Cloud Starter の間の往復遅延と、1 リクエストあたりの SQL の回数を変えて応答時間を計測しました。応答時間の増分は、往復遅延と逐次の往復回数の積でおおむね決まってくると分かりました。SQL の集約で応答時間を 65% 以上、接続の使い回しで 70% 以上削減できました。

---

*この記事は自動収集システムによって保存されました。*
