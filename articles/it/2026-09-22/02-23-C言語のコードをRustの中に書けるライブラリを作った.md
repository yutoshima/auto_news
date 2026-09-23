---
title: "C言語のコードをRustの中に書けるライブラリを作った"
source: "Zenn"
category: "it"
published: 2026-09-22T02:23:29
url: https://zenn.dev/tanakh/articles/c-code-in-rust
---

# C言語のコードをRustの中に書けるライブラリを作った

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年09月22日 02:23
- **URL**: [https://zenn.dev/tanakh/articles/c-code-in-rust](https://zenn.dev/tanakh/articles/c-code-in-rust)

## 概要

C言語のコードをRustの中に書けるようにするライブラリ cinrs を作りました。
https://github.com/tanakh/cinrs
https://crates.io/crates/cinrs
こんな風にCのコードをRustの中に書いて、Rustから呼び出したりできます。
use cinrs::c99;

c99! {
    int fact(int n) {
        return n == 0 ? 1 : n * fact(n - 1);
    }
}

println!("fact(10) = {}", unsafe { fact(10) }); // ...

---

*この記事は自動収集システムによって保存されました。*
