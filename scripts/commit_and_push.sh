#!/usr/bin/env bash
# 記事をコミットして main へ push する。
# 他のワークフローや手動 push と同時に動いても失敗しないよう、
# 最新の main を取り込み直してから push し、失敗したらやり直す。
#
# 使い方: scripts/commit_and_push.sh "コミットメッセージ"
set -uo pipefail

MESSAGE="$1"
BRANCH="main"
MAX_ATTEMPTS=10

git config user.name "GitHub Actions Bot"
git config user.email "actions@github.com"

git add articles/
if git diff --staged --quiet; then
  echo "変更なし"
  exit 0
fi
git commit -q -m "$MESSAGE"

for i in $(seq 1 "$MAX_ATTEMPTS"); do
  # 最新の main の上に自分のコミットを載せ直す。
  # 同じ記事ファイルを双方が書いていた場合は、今回の実行の内容を優先する
  # （rebase 中の "theirs" は載せ直している自分のコミット側）。
  if git pull -q --rebase -X theirs origin "$BRANCH" && git push -q origin "HEAD:$BRANCH"; then
    echo "push成功 (${i}回目)"
    exit 0
  fi

  # 途中で止まった rebase が残ると以降のリトライがすべて失敗するため片付ける
  git rebase --abort 2>/dev/null || true

  wait=$((i * 5 + RANDOM % 10))
  echo "push失敗 (${i}/${MAX_ATTEMPTS}回目)、${wait}秒後にリトライします"
  sleep "$wait"
done

echo "::error::${MAX_ATTEMPTS}回試してもpushできませんでした"
exit 1
