import discord
from discord.ext import commands
import json
from dotenv import load_dotenv
import os
import requests
import random
import time

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


    @commands.command()
    async def sticker(self, ctx:commands.Context, *, search: str):
        search = search.replace(" ", "+")
        response = requests.get('http://api.giphy.com/v1/stickers/search?q=' + search + '&api_key=' + GIPHY_TOKEN + '&limit=50' +'&rating=g')
        data = json.loads(response.text)
        gif_choice = random.randint(0, len(data['data'])-1)
        result_gif = data['data'][gif_choice]['images']['original']['url']
        await ctx.send(embed=discord.Embed(color=0x9c13ae).set_image(url=result_gif).set_footer(text=f"Requested by: {ctx.author.name}", icon_url=ctx.author.avatar_url))


    @commands.command(pass_context=True)
    async def woof(self, ctx):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = json.loads(response.text)
        await ctx.send(embed=discord.Embed(title="Woof woof! 🐶", color=discord.Colour.magenta()).set_image(url=f"{data['message']}"))
    
    
    @commands.command(pass_context=True)
    async def meow(self, ctx):
        response = requests.get("https://nekos.life/api/v2/img/meow")
        data = json.loads(response.text)
        await ctx.send(embed=discord.Embed(title="Meooow! 🐱", color=discord.Colour.magenta()).set_image(url=f"{data['url']}"))

    @commands.command(pass_context=True)
    async def quack(self, ctx):
        response = requests.get("https://random-d.uk/api/v2/random")
        data = json.loads(response.text)
        await ctx.send(embed=discord.Embed(title="Quaaack! 🦆", color=discord.Colour.magenta()).set_image(url=f"{data['url']}"))

    @commands.command(pass_context=True)
    async def bunny(self, ctx):
        response = requests.get("https://api.bunnies.io/v2/loop/random/?media=gif")
        data = json.loads(response.text)
        await ctx.send(embed=discord.Embed(title="Sniiiff! 🐰", color=discord.Colour.magenta()).set_image(url=f"{data['media']['gif']}"))

    
    @commands.command(pass_context=True)
    async def frog(self, ctx):
        response = requests.get("https://pixabay.com/api/?key=21235030-93835b5c477d07feab3263cad&q=frog&per_page=100")
        data = json.loads(response.text)
        choice = random.choice(data['hits'])
        url = choice['webformatURL']
        await ctx.send(embed=discord.Embed(title="Riiibbit! 🐸", color=discord.Colour.magenta()).set_image(url=url))

    @commands.command(pass_context=True)
    async def fox(self, ctx):
        response = requests.get("https://randomfox.ca/floof/")
        data = json.loads(response.text)
        await ctx.send(embed=discord.Embed(title="Booop! 🦊", color=discord.Colour.magenta()).set_image(url=f"{data['image']}"))

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        response = requests.get("https://meme-api.herokuapp.com/gimme")
        data = json.loads(response.text)
        while data['nsfw'] == 'false':
            response = requests.get("https://meme-api.herokuapp.com/gimme")
            data = json.loads(response.text)
        await ctx.send(embed=discord.Embed(title=f"\"{data['title']}\"", color=discord.Colour.magenta()).set_image(url=f"{data['url']}"))


def setup(bot:commands.Bot):
    bot.add_cog(Post(bot))