import discord
from discord.ext import commands
import time


class Psych(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def psych(self, ctx:commands.Context):
        blob = "<a:partyblob:833310816806633473>"
        await ctx.send(f"***PSYCH!!*** {blob * 6}")


    
    @commands.command()
    async def selfdestruct(self, ctx):
        user = await self.bot.fetch_user(827499950304657418)
        if ctx.author.id != 225530876761473025:
            await ctx.send("https://tenor.com/view/inauguration-cnn2017-donald-trump-finger-wag-no-gif-7576946")
            return
        await ctx.send("Are you sure you want to do that? :flushed: ")
        msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        if msg.content.lower() == 'yes':
            await ctx.send("Welp, so this is it..... :cry: It has been a good run!")
            time.sleep(1)
            await ctx.send(embed=discord.Embed(description="***Self Destruct Initiated!*** *Please follow the evacuation protocol!*", color=discord.Colour.magenta()))
            msg = await ctx.send(embed=discord.Embed(description="**Self Destructing in**..... 20", color=discord.Colour.magenta()))
            for i in range(1,21):
                time.sleep(1.5)
                if i == 5:
                    await ctx.send("https://tenor.com/view/up-love-carl-fredricksen-ellie-fredricksen-clouds-gif-7342022")
                    await ctx.send("(🎵 *Playing 'Married life' from 'UP')*")
                if i == 10:
                    await ctx.send("https://tenor.com/view/up-carl-ellie-carlellie-gif-4588842")
                if i == 15:
                    await ctx.send("*Were I a good bot?*")
                    await ctx.send("https://tenor.com/view/disney-up-mr-fredrickson-ellie-memories-gif-7957249")
                await msg.edit(embed=discord.Embed(description=f"Self Destructing in..... {20 - i}", color=discord.Colour.magenta()))
                #await ctx.send(embed=discord.Embed(title=20-i, color=0x9c13ae))
            await ctx.send("So long partner! :smiling_face_with_tear:")
            time.sleep(2)
            await ctx.send("https://tenor.com/view/chicken-chicken-bro-destroy-boom-explosion-gif-14109606")
            time.sleep(3)
            embed=discord.Embed(description=f"Uh oh, {user.mention} has left the server <:pikatears:824738880095912017>! We have {len(ctx.message.author.guild.members)-1} members now! <:icri:793199677582999582>", color=discord.Colour.magenta())
            embed.set_image(url="https://media.giphy.com/media/26u4b45b8KlgAB7iM/giphy.gif")
            await self.bot.change_presence(status=discord.Status.offline)
            await ctx.send(embed=embed)
            time.sleep(5)
            blob = "<a:partyblob:833310816806633473>"
            await ctx.send(f"***PSYCH!!*** {blob * 6} <:kekw:826828175946022942>")
            await ctx.send(embed=discord.Embed(color=discord.Colour.magenta()).set_image(url="https://media1.tenor.com/images/774db5013329cf8826516e20a8c99101/tenor.gif?itemid=9405008"))
        else:
            await ctx.send("*Phew!*")
            await ctx.send("https://tenor.com/view/spongebob-squarepants-nickelodeon-sigh-phew-gif-5752975")


    @commands.command()
    async def set_status(self, ctx:commands.Context, _status: str):
        if _status.lower() == "online":
            await self.bot.change_presence(status=discord.Status.online)
            #print("set status to online")
        elif _status.lower() == "offline":
            await self.bot.change_presence(status=discord.Status.offline)
            #print("set status to offline")
        elif _status.lower() == "idle":
            await self.bot.change_presence(status=discord.Status.idle)
            #print("set status to idle")
        elif _status.lower() == "dnd":
            await self.bot.change_presence(status=discord.Status.do_not_disturb)
            #print("set status to dnd")

def setup(bot:commands.Bot):
    bot.add_cog(Psych(bot))