#!/bin/bash
# Discord Bot起動スクリプト

echo "🤖 Discord Botを起動します..."
echo ""

# 仮想環境をアクティベート（存在する場合）
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Botを起動
python discord_bot.py
