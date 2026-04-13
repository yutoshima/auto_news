---
title: "Ingress NGINXの退役に伴うGateway API + Envoy Gatewayへの移行"
source: "Zenn"
category: "it"
published: 2026-04-13T03:44:32
url: https://zenn.dev/mitene/articles/202604-ingress-nginx-to-envoy-gateway
---

# Ingress NGINXの退役に伴うGateway API + Envoy Gatewayへの移行

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月13日 03:44
- **URL**: [https://zenn.dev/mitene/articles/202604-ingress-nginx-to-envoy-gateway](https://zenn.dev/mitene/articles/202604-ingress-nginx-to-envoy-gateway)

## 概要

こんにちは、『家族アルバム みてね』（以下、みてね）でSREを担当している @kohbis です。
皆さんご存知のとおり、2026年3月にKubernetes Ingress Controllerのkubernetes/ingress-nginxはretirementとなり、すでにリポジトリもパブリックアーカイブされています。
https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/
みてねでも、ingress-nginxを活用していたため、retirementに伴う移行を検討する必要がありました。
ただし、ユーザー向...

---

*この記事は自動収集システムによって保存されました。*
