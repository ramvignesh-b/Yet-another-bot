import discord
from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role('Owners')
    async def purge(self, ctx, amount=2):
        if amount > 100:
            await ctx.send("https://tenor.com/view/blank-stare-really-i-dont-believe-you-side-eye-looking-gif-6151149")
            await ctx.send("Seriously?! *smh* `-_-`")
        else:
            await ctx.channel.purge(limit=amount)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            if ctx.message.author.id == 225530876761473025:
                number = ctx.message.content[7:]
                await ctx.channel.purge(limit=int(number))
            else:
                await ctx.send(embed=discord.Embed(description=f"Sorry, I can't accept the command from you yet, {ctx.author.mention} <:MiniCrewmate:776474173870571550>", color=0x9c13ae))


def setup(bot):
    bot.add_cog(CogName(bot))