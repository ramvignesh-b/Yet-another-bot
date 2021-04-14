import discord
from discord.ext import commands
from asyncdagpi import Client, ImageFeatures
import requests
from PIL import Image, ImageDraw, ImageOps
from dotenv import load_dotenv
import os
from io import BytesIO


DAGPI_TOKEN = os.getenv('DAGPI_TOKEN')
ALEX_TOKEN = os.getenv('ALEX_TOKEN')

headers = {
    'Authorization':ALEX_TOKEN
}


class Images(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def stab(self, ctx:commands.Context, user:discord.Member, user2:discord.Member = None):
        await ctx.message.delete()
        if user2 != None:
            img1 = requests.get(user2.avatar_url_as(format="png"))
        else:
            img1 = requests.get(ctx.author.avatar_url_as(format="png"))
        img2 = requests.get(user.avatar_url_as(format="png"))
        p1 = Image.open(BytesIO(img1.content)).convert('RGB')
        p2 = Image.open(BytesIO(img2.content)).convert('RGB')
        img = Image.open("assets/img/knife.png")
        draw = ImageDraw.Draw(img)
        p1 = p1.resize((180, 180), Image.ANTIALIAS)
        p2 = p2.resize((180, 180), Image.ANTIALIAS)
        bigsize = (p1.size[0] * 4, p1.size[1] * 4)
        mask = Image.new('L', bigsize, 0)
        draw1 = ImageDraw.Draw(mask)
        draw1.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(p1.size, Image.ANTIALIAS)
        p1.putalpha(mask)
        p2.putalpha(mask)
        img.paste(p1, (200, 80), p1)
        img.paste(p2, (425, 85), p2)
        #img.show()
        img.save(f"Temp/knife_{ctx.author.id}.png")
        file=discord.File(f"Temp/knife_{ctx.author.id}.png")
        embed = discord.Embed(color=discord.Colour.magenta()).set_image(url=f"attachment://knife_{ctx.author.id}.png")
        await ctx.send(file=file, embed=embed)


    @commands.command()
    async def trigger(self, ctx, user: discord.Member = None):
        dagpi = Client(DAGPI_TOKEN)
        if user == None:
            url = ctx.author.avatar_url_as(format="png")
        else:
            url = user.avatar_url_as(format="png")
        img = await dagpi.image_process(ImageFeatures.triggered(), str(url))
        await dagpi.close()
        file = discord.File(fp=img.image,filename=f"pixel.{img.format}")
        embed = discord.Embed(color=discord.Colour.magenta()).set_image(url=f"attachment://pixel.{img.format}")
        await ctx.send(file=file, embed=embed)

    
    @commands.command()
    async def fact(self, ctx, *, message):
        await ctx.message.delete()
        response = requests.get(url="https://api.alexflipnote.dev/facts?text="+message, headers=headers)
        byte = BytesIO(response.content)
        image = Image.open(byte)
        image.save(f"Temp/fact_{ctx.author.id}.png","png")
        file=discord.File(f"Temp/fact_{ctx.author.id}.png")
        embed = discord.Embed(color=discord.Colour.magenta()).set_image(url=f"attachment://fact_{ctx.author.id}.png")
        await ctx.send(file=file, embed=embed)


    @commands.command()
    async def drake(self, ctx, message1, message2):
        await ctx.message.delete()
        response = requests.get(url=f"https://api.alexflipnote.dev/drake?top={message1}&bottom={message2}", headers=headers)
        byte = BytesIO(response.content)
        image = Image.open(byte)
        #image.show()
        image.save(f"Temp/drake_{ctx.author.id}.png","png")
        file=discord.File(f"Temp/drake_{ctx.author.id}.png")
        embed = discord.Embed(color=discord.Colour.magenta()).set_image(url=f"attachment://drake_{ctx.author.id}.png")
        await ctx.send(file=file, embed=embed)


    @commands.command()
    async def kick(self, ctx, user: discord.Member, user2: discord.Member = None):
        roles = ['cyan', 'brown', 'red', 'blue', 'black', 'yellow', 'lime', 'green', 'white', 'purple', 'orange', 'pink']
        await ctx.message.delete()
        if user2 != None:
            img1 = requests.get(user2.avatar_url_as(format="png"))
        else:
            img1 = requests.get(ctx.author.avatar_url_as(format="png"))
        img2 = requests.get(user.avatar_url_as(format="png"))
        p1 = Image.open(BytesIO(img1.content)).convert('RGB')
        p2 = Image.open(BytesIO(img2.content)).convert('RGB')
        img = Image.open("assets/img/kick/kick.png")
        draw = ImageDraw.Draw(img)
        p1 = p1.resize((300, 300), Image.ANTIALIAS)
        p1 = p1.rotate(10)
        p2 = p2.resize((180, 180), Image.ANTIALIAS)
        p2 = p2.rotate(40)
        bigsize = (p1.size[0] * 4, p1.size[1] * 4)
        mask = Image.new('L', bigsize, 0)
        draw1 = ImageDraw.Draw(mask)
        draw1.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(p1.size, Image.ANTIALIAS)
        p1.putalpha(mask)
        bigsize = (p2.size[0] * 4, p2.size[1] * 4)
        mask = Image.new('L', bigsize, 0)
        draw1 = ImageDraw.Draw(mask)
        draw1.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(p2.size, Image.ANTIALIAS)
        p2.putalpha(mask)
        color = ''
        user_role = user.roles
        for role in user_role:
            if role.name.lower() in roles:
                color = role.name.lower()
                break
        if color != '':
            k2 = Image.open(f"assets/img/kick/kickee_{color}.png")
            img.paste(k2, (0,0), k2)

        color = ''
        if user2 != None:
            user_role = user2.roles
        else:
            user_role = ctx.author.roles
        for role in user_role:
            if role.name.lower() in roles:
                color = role.name.lower()
                break
        if color != '':
            k1 = Image.open(f"assets/img/kick/kicker_{color}.png")
            img.paste(k1, (0,0), k1)        
        t1 = Image.open("assets/img/kick/tear.png")
        t1 = t1.resize((int(t1.size[0] / 8.5), int(t1.size[1] / 8.5)), Image.ANTIALIAS)
        t1 = t1.rotate(-15)
        t2 = t1.rotate(-70)
        t2 = t2.resize((int(t1.size[0] / 1.3), int(t1.size[1] / 1.3)), Image.ANTIALIAS)
        t2 = ImageOps.mirror(t2)
        img.paste(p1, (190, 300), p1)
        img.paste(p2, (675, 105), p2)
        img.paste(t1, (680, 200), t1)
        img.paste(t2, (820, 110), t2)
        ang = Image.open("assets/img/kick/angry.png").convert('RGBA')
        ang = ang.resize((int(ang.size[0] / 4), int(ang.size[1] / 4)), Image.NEAREST)
        img.paste(ang, (120, 350), ang)
        #img.show()
        img.save(f"Temp/kick_{ctx.author.id}.png")
        file=discord.File(f"Temp/kick_{ctx.author.id}.png")
        embed = discord.Embed(color=discord.Colour.magenta()).set_image(url=f"attachment://kick_{ctx.author.id}.png")
        await ctx.send(file=file, embed=embed)

    
    @commands.command()
    async def trash(self, ctx, user:discord.Member):
        await ctx.message.delete()
        img1 = ctx.author.avatar_url_as(format="png")
        img2 = user.avatar_url_as(format="png")
        response = requests.get(url=f"https://api.alexflipnote.dev/trash?face={img1}&trash={img2}", headers=headers)
        byte = BytesIO(response.content)
        image = Image.open(byte)
        image.save(f"Temp/trash_{user.id}.png","png")
        file=discord.File(f"Temp/trash_{user.id}.png")
        embed = discord.Embed(color=discord.Colour.magenta()).set_image(url=f"attachment://trash_{user.id}.png")
        await ctx.send(file=file, embed=embed)


    @commands.command()
    async def bigtext(self, ctx, *, message):
        await ctx.message.delete()
        response = requests.get(url=f"https://api.alexflipnote.dev/supreme?text={message}&dark=true", headers=headers)
        byte = BytesIO(response.content)
        image = Image.open(byte)
        image.save(f"Temp/bigt_{ctx.author.id}.png","png")
        await ctx.send(file=discord.File(f"Temp/bigt_{ctx.author.id}.png"))
        

def setup(bot:commands.Bot):
    bot.add_cog(Images(bot))