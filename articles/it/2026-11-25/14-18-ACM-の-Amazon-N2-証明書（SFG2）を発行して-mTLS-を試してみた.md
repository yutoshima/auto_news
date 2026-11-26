---
title: "ACM の Amazon N2 証明書（SFG2）を発行して mTLS を試してみた"
source: "DevelopersIO"
category: "it"
published: 2026-11-25T14:18:35
url: https://dev.classmethod.jp/articles/acm-amazon-n2-certificates-mtls/
---

# ACM の Amazon N2 証明書（SFG2）を発行して mTLS を試してみた

## メタデータ

- **情報源**: DevelopersIO
- **カテゴリ**: it
- **公開日時**: 2026年11月25日 14:18
- **URL**: [https://dev.classmethod.jp/articles/acm-amazon-n2-certificates-mtls/](https://dev.classmethod.jp/articles/acm-amazon-n2-certificates-mtls/)

## 概要

ACM で発行できる Amazon N2 証明書には、ルート階層が2種類あります。SFG2 階層を発行して、拡張キー使用法に clientAuth が含まれることと、OpenSSL で mTLS が成立することを確かめました。ACM の証明書をクライアント認証にも使えますが、検証する側にルートの追加が必要です。

---

*この記事は自動収集システムによって保存されました。*
