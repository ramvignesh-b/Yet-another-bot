import discord
from discord.ext import commands
import json



class Rules(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        with open('assets/rules/rules.json') as f:
            self.rules = json.load(f)


    @commands.command()
    async def postRules(self, ctx:commands.Context):
        file=discord.File("assets/rules/welcome.png",filename="welcome.png")
        await ctx.send(file=file)
        embed=discord.Embed(description="This small community server is aimed at creating an emotional haven for people all around the world to socialize and play with, whilst having fun. We started with Among Us and gradually started playing other party games as well.", color=0x9c13ae)
        await ctx.send(embed=embed)
        file=discord.File("assets/rules/rules.png",filename="rules.png")
        await ctx.send(file=file)
        embed=discord.Embed(description="We request you to adhere to certain rules in the server for a better and safe experience. Don't worry, we don't ask much 😇!", color=0x9c13ae)
        for i in range (0, len(self.rules)):
            embed.add_field(name="\u200b", value=f"{i + 1}. {self.rules[i]['rule']}", inline=False)
        embed.add_field(name="\u200b", value=f"\u200b", inline=False)
        embed.add_field(name="Feel free to share your stories, accomplishments and emotions with us. \nHave a pleasant day! 💖", value=f"\u200b")
        await ctx.send(embed=embed)


def setup(bot:commands.Bot):
    bot.add_cog(Rules(bot))