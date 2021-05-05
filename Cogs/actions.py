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
        embed = discord.Embed(description=f"{ctx.author.mention} hugged {user.mention}! <a:pingu_hug:823864118117007390>", color=discord.Colour.magenta())
        await ctx.send(embed=embed.set_image(url=f"{data['url']}").set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url))


def setup(bot:commands.Bot):
    bot.add_cog(Actions(bot))