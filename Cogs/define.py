import discord
from discord.ext import commands
import requests
import json

class Define(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, ctx, message):
        term = message.replace(" ", "+")
        response = requests.get(
            'http://api.urbandictionary.com/v0/define?term=' + term)
        data = json.loads(response.text)
        try:
            definition = data['list'][0]['definition'].replace("[", "")
            embed = discord.Embed(title=f"Definition of \"{message}\"", url=data['list'][0]['permalink'], description=definition.replace(
                "]", ""), color=discord.Colour.magenta())
            await ctx.send(embed=embed)
        except:
            await ctx.send("Nothing found ┬─┬ ノ( ゜-゜ノ)")


def setup(bot):
    bot.add_cog(Define(bot))