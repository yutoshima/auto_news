---
title: "SwiftDataのrollback()、iOS 27で黙って挙動が変わっていた"
source: "Zenn"
category: "it"
published: 2026-10-13T14:09:49
url: https://zenn.dev/kzq/articles/swiftdata-rollback-ios27
---

# SwiftDataのrollback()、iOS 27で黙って挙動が変わっていた

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年10月13日 14:09
- **URL**: [https://zenn.dev/kzq/articles/swiftdata-rollback-ios27](https://zenn.dev/kzq/articles/swiftdata-rollback-ios27)

## 概要

個人開発しているゲームアプリのテストを、iOS 27 のシミュレータで回してみた。いつもは iOS 26.5 で回していて、そこでは通っているテストだ。
落ちたのは、ミッション報酬の受け取りで save に失敗したときに Gold が元に戻るかを見るテストだった。期待値は「受け取る前の Gold」なのに、実際はそれより少ない。報酬を足して、save に失敗して、戻したら、足した分より多く引かれていた。
最初はこっちのバグを疑った。でもコードもビルドも同じで、変えたのはシミュレータの OS だけ。調べていくと、SwiftData の ModelContext.rollback() の挙動が...

---

*この記事は自動収集システムによって保存されました。*
