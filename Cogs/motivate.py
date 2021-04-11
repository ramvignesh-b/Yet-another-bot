import discord
from discord.ext import commands
import requests
import json


class Motivate(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def motivate(self, ctx:commands.Context, user: discord.Member = None):
        response = requests.get('https://www.affirmations.dev/')
        data = json.loads(response.text)
        if user != None:
            text = user.mention
        else:
            text = ctx.author.mention
        quote = f"Hey, {text}! **{data['affirmation']}** :)"
        embed = discord.Embed(description=quote, color=discord.Colour.magenta())
        await ctx.send(embed=embed)

    @commands.command()
    async def quote(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        embed = discord.Embed(color=discord.Colour.magenta()).set_footer(text="Courtesy: ZenQuotes.io")
        embed.add_field(name=f'"{quote}"', value=f"~{author}")
        await ctx.send(embed=embed)


def setup(bot:commands.Bot):
    bot.add_cog(Motivate(bot))