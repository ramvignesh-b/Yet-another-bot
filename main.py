import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()


BOT_PREFIX = ('k!')
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
bot = Bot(command_prefix=BOT_PREFIX, intents=intents)


if __name__ == '__main__':
    for filename in os.listdir("Cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"Cogs.{filename[:-3]}")


@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")

bot.run(TOKEN)