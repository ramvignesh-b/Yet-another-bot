import discord
from discord.ext import commands
import requests
import json


class Define(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def urb(self, ctx, message):
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


    @commands.command()
    async def define(self, ctx, *, message):
        word = message.replace(" ", "+")
        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/'  + word.lower()
        response = requests.get(url, headers = {'app_id' : '486f551b', 'app_key' : '072360529cf5423239dd6af3e7f87d4a'})
        data = json.loads(response.text)
        #print(data)
        try:
            definition = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
            embed = discord.Embed(title=f"Definition of \"{message}\"", description=definition, color=discord.Colour.magenta())
            await ctx.send(embed=embed)
        except:
            await ctx.send("Nothing found ┬─┬ ノ( ゜-゜ノ)")


def setup(bot):
    bot.add_cog(Define(bot))