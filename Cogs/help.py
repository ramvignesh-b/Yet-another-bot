import discord
from discord.ext import commands
import json


class Help(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx:commands.Context):
        embed = discord.Embed(title="List of commands", description="**__Prefix:__** `k!` ", color=discord.Colour.magenta())
        with open('assets/help.json', encoding='utf-8') as f:
            command_list = json.load(f)
        split = len(command_list)
        for i in range(0, split):
            embed.add_field(name=f"{command_list[i]['command']}", value=command_list[i]['help'], inline=False)
        await ctx.send(embed=embed)


def setup(bot:commands.Bot):
    bot.add_cog(Help(bot))