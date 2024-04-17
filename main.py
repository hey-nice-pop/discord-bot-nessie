import discord
from discord.ext import commands
import config

import game.othello as othello

YOUR_BOT_TOKEN = config.BOT_TOKEN

# インテントを有効化
intents = discord.Intents.all()

# Botオブジェクトの生成
bot = commands.Bot(
    command_prefix='/', 
    intents=intents, 
    sync_commands=True,
    activity=discord.Game("水風呂")
)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'ログイン完了: {bot.user}')

# コマンドをothello.pyから読み込む
othello.setup(bot)

# Discordボットを起動
bot.run(YOUR_BOT_TOKEN)
