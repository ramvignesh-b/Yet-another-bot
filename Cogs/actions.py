import discord
from discord.ext import commands
import requests
import json


class Actions(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def hug(self, ctx, user: discord.Member):
        response = requests.get("https://nekos.life/api/hug")
        data = json.loads(response.text)
        await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} hugged {user.mention}!🤗", color=discord.Colour.magenta()).set_image(url=f"{data['url']}"))


def setup(bot:commands.Bot):
    bot.add_cog(Actions(bot))