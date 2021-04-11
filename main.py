import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv
from cogwatch import Watcher


load_dotenv()


BOT_PREFIX = ('k!')
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
intents.members = True

bot = Bot(command_prefix=BOT_PREFIX, intents=intents)

bot.remove_command("help")

@bot.event
async def on_ready():
    print('Bot ready.')
    watcher = Watcher(bot, path='Cogs')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over Kinda Sus"))
    await watcher.start()


if __name__ == '__main__':
    for filename in os.listdir("Cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"Cogs.{filename[:-3]}")


@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")

bot.run(TOKEN)