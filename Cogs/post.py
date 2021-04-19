import discord
from discord.ext import commands
import json
from dotenv import load_dotenv
import os
import requests
import random


load_dotenv()

GIPHY_TOKEN = os.environ.get('GIPHY_TOKEN')

class Post(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def gif(self, ctx:commands.Context, *, search: str):
        search = search.replace(" ", "+")
        response = requests.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=' + GIPHY_TOKEN + '&limit=50' +'&rating=g')
        data = json.loads(response.text)
        gif_choice = random.randint(0, len(data['data'])-1)
        result_gif = data['data'][gif_choice]['images']['original']['url']
        await ctx.send(embed=discord.Embed(color=0x9c13ae).set_image(url=result_gif).set_footer(text=f"Requested by: {ctx.author.name}", icon_url=ctx.author.avatar_url))


    @commands.command(pass_context=True)
    async def woof(self, ctx):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = json.loads(response.text)
        await ctx.send(embed=discord.Embed(title="Woof woof! 🐶", color=0x9c13ae).set_image(url=f"{data['message']}"))
    
    
    @commands.command(pass_context=True)
    async def meow(self, ctx):
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = json.loads(response.text)
        await ctx.send(embed=discord.Embed(title="Meooow! 🐱", color=0x9c13ae).set_image(url=f"{data[0]['url']}"))


def setup(bot:commands.Bot):
    bot.add_cog(Post(bot))