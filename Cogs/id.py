import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO

class ID(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def id(self, ctx:commands.Context, user: discord.Member = None):
        roles = ['cyan', 'brown', 'red', 'blue', 'black', 'yellow', 'lime', 'green', 'white', 'purple', 'orange', 'pink']
        if user == None:
            user = ctx.message.author
        img = Image.open("assets/profile/id.png")
        draw = ImageDraw.Draw(img)
        font2 = ImageFont.truetype("assets/welcome/amatic-sc.bold.ttf", 40)
        font = ImageFont.truetype("assets/welcome/amatic-sc.bold.ttf", 40)
        color = (1, 1, 1)
        color2 = (204, 51, 6)
        draw.text((300, 160), "Name: ", color2, font=font2)
        draw.text((300, 220), "ID: ", color2, font=font2)
        draw.text((300, 280), "Joined: ", color2, font=font2)
        draw.text((300, 340), "Nickname: ", color2, font=font2)
        draw.text((300, 400), "Top Role: ", color2, font=font2)
        draw.text((420, 160), "{}".format(user.name), color, font=font)
        draw.text((420, 220), "{}".format(user.id), color, font=font)
        draw.text((420, 280), "{}".format(
            user.joined_at.strftime("%B %d, %Y")), color, font=font)
        draw.text((420, 340), "{}".format(user.display_name), color, font=font)
        if user.top_role.name.lower() in roles:
            top_role = user.roles[-2].name
        else:
            top_role = user.top_role

        draw.text((420, 400), "{}".format(top_role), color, font=font)
        response = requests.get(user.avatar_url_as(format='png'))
        profile = Image.open(BytesIO(response.content))
        profile = profile.resize((170, 170), Image.ANTIALIAS)
        bigsize = (profile.size[0] * 3, profile.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw1 = ImageDraw.Draw(mask)
        draw1.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(profile.size, Image.ANTIALIAS)
        profile.putalpha(mask)

        color = ''
        user_role = user.roles
        #print(user_role)
        for role in user_role:
            if role.name.lower() in roles:
                color = role.name.lower()
                break
        #print(color)
        if color != '':
            crew = Image.open(f"assets/img/{color}.png")
            img.paste(crew, (70,350), crew)
        img.paste(profile, (50, 150), profile)
        img.save(f"Temp/user_id_{ctx.author.id}.png")
        file=discord.File(f"Temp/user_id_{ctx.author.id}.png", filename=f"id_{ctx.author.id}.png")
        await ctx.send(file=file, embed=discord.Embed(title=f"Kinda Sus ID", color=discord.Colour.magenta()).set_image(url=f"attachment://id_{ctx.author.id}.png").set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url))


def setup(bot:commands.Bot):
    bot.add_cog(ID(bot))