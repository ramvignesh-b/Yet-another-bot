import discord
from discord.ext import commands
import random

class Giveaway(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def giveaway(self, ctx:commands.Context, title, text, end):
        await ctx.send(f"@here A new giveaway has been started. React with '🎟️' to participate.")
        embed = discord.Embed(title=title, description=text, color=discord.Colour.magenta())
        embed.add_field(name="Ends on", value=end)
        embed.set_footer(text=f"Started by {ctx.author}", icon_url=ctx.author.avatar_url)
        message = await ctx.send(embed=embed)
        await message.add_reaction('🎟️')
    
    
    @commands.command(name = "pickwinner")
    async def pickwinner(self, ctx, num: int, id: int):
        message = await ctx.fetch_message(id)
        """
        if message.author.id != ctx.author.id:
            await ctx.send(f"❌ You can only pick the winner for the giveaways started by you, {ctx.author.mention}")
            return 
        """
        if message.reactions == []:
            await ctx.send(f"❌ Not a valid Giveaway message!")
            return
        elif message.reactions[0].emoji != '🎟️':
            await ctx.send(f"❌ Not a valid Giveaway message!")
            return
        users = await message.reactions[0].users().flatten()
        if num <= len(users):
            embed=discord.Embed(title='Giveaway Winners', description=f"Here's the list of winner(s). Congratulations! 🎉", color=discord.Colour.magenta())
            number = num
            del users[0]
            for i in range(num):
                choice = random.randint(0, number-1)
                number -= 1
                if(i == num-1):
                    choice = 0
                winner = users[choice]
                del users[choice]
                embed.add_field(name=f"\u200b", value=f"{i+1}) <@{winner.id}>")
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=discord.Embed(description=f"Error while picking a winner! Less no. of participants!", color=discord.Colour.magenta()))
        await ctx.message.delete()


def setup(bot:commands.Bot):
    bot.add_cog(Giveaway(bot))