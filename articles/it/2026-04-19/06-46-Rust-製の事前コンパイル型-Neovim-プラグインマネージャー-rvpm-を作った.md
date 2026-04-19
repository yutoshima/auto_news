---
title: "Rust 製の事前コンパイル型 Neovim プラグインマネージャー rvpm を作った"
source: "Zenn"
category: "it"
published: 2026-04-19T06:46:40
url: https://zenn.dev/yukimemi/articles/2026-04-19-rvpm
---

# Rust 製の事前コンパイル型 Neovim プラグインマネージャー rvpm を作った

## メタデータ

- **情報源**: Zenn
- **カテゴリ**: it
- **公開日時**: 2026年04月19日 06:46
- **URL**: [https://zenn.dev/yukimemi/articles/2026-04-19-rvpm](https://zenn.dev/yukimemi/articles/2026-04-19-rvpm)

## 概要

自作の Neovim プラグインマネージャー rvpm を Claude Code と一緒に作りました。Rust 製で、設定ファイル (config.toml) から静的な loader.lua を事前コンパイルする CLI ファーストな設計になっています。
https://github.com/yukimemi/rvpm


 なぜ新しく作ったのか
以前、Deno + denops ベースの dvpm を作り、愛用していました（過去の記事・キャッシュ機能の記事）。dvpm は denops との親和性も高く気に入っていたのですが、使い続けるうちにいくつか気になる点が出てきました。


...

---

*この記事は自動収集システムによって保存されました。*
