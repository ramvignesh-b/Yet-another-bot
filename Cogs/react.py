import discord
from discord.ext import commands


class React(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def react(self, ctx:commands.Context, id):
        await ctx.message.delete()
        message = await ctx.fetch_message(id)
        await message.add_reaction('<a:partyblob:815199485096493057>')
        


def setup(bot:commands.Bot):
    bot.add_cog(React(bot))