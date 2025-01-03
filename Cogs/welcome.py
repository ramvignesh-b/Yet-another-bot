import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO


class Welcome(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member: discord.member):
        if member.guild.id != 793117819000717322:
            return
        embed = discord.Embed(description=f"Hey {member.mention}, we hope you'll like your stay at **Kinda Sus** <a:PikaLove:830682688985104474>! Have a wonderful day <a:party_blob:826828706843721758>!", color=discord.Colour.magenta())
        img = Image.open("assets/welcome/welcome.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("assets/welcome/amatic-sc.bold.ttf", 80)
        font2 = ImageFont.truetype("assets/welcome/amatic-sc.regular.ttf", 40)
        draw.text((150, 5), f"{member.name} !", (255, 255, 255), font=font)
        n = len(member.guild.members)
        suffix = { 1: "st", 2: "nd", 3: "rd" }.get(n if (n < 20) else (n % 10), 'th')
        draw.text((300, 414), f"You're  our  {str(n) + suffix}  member!", (255, 255, 255), font=font2)
        response = requests.get(member.avatar_url_as(format="png"))
        profile = Image.open(BytesIO(response.content))
        profile = profile.resize((120, 120), Image.ANTIALIAS)
        bigsize = (profile.size[0] * 3, profile.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw1 = ImageDraw.Draw(mask)
        draw1.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(profile.size, Image.ANTIALIAS)
        profile.putalpha(mask)
        img.paste(profile, (50, 146), profile)
        img.save(f'Temp/welcome.png', 'png')
        file=discord.File('Temp/welcome.png', filename="welcome.png")
        embed.set_image(url="attachment://welcome.png")
        await member.guild.get_channel(793142615793074236).send(file=file, embed=embed)


    @commands.Cog.listener()
    async def on_member_remove(self, member:discord.Member):
        if member.guild.id != 793117819000717322:
            return
        embed=discord.Embed(description=f"Uh oh, {member.mention} has left the server <:pikatears:824738880095912017>! We have {len(member.guild.members)} members now! <:icri:793199677582999582>", color=discord.Colour.magenta())
        embed.set_image(url="https://media.giphy.com/media/26u4b45b8KlgAB7iM/giphy.gif")
        await member.guild.get_channel(793142615793074236).send(embed=embed)


def setup(bot:commands.Bot):
    bot.add_cog(Welcome(bot))