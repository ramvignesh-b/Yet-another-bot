import discord
from discord.ext import commands
from dpymenus import Page, PaginatedMenu
import json


class Help(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx:commands.Context):
        page1 = Page(title="List of commands", description="__Page 1__: **General Commands**", color=discord.Colour.magenta())
        with open('assets/help.json', encoding='utf-8') as f:
            command_list = json.load(f)
        for i in range(0, len(command_list)):
            page1.add_field(name=f"{command_list[i]['command']}", value=command_list[i]['help'], inline=False)
        
        page2 = Page(title="List of commands", description="__Page 2__ **Image Commands**", color=discord.Colour.magenta())
        with open('assets/images.json', encoding='utf-8') as f:
            command_list = json.load(f)
        for i in range(0, len(command_list)):
            page2.add_field(name=f"{command_list[i]['command']}", value=command_list[i]['help'], inline=False)
        
        page3 = Page(title="List of commands", description="__Page 3__ **Animals Commands**", color=discord.Colour.magenta())
        with open('assets/animals.json', encoding='utf-8') as f:
            command_list = json.load(f)
        for i in range(0, len(command_list)):
            page3.add_field(name=f"{command_list[i]['command']}", value=command_list[i]['help'], inline=False)
        
        menu = PaginatedMenu(ctx).allow_multisession()
        menu.add_pages([page1, page2, page3])
        await menu.open()


def setup(bot:commands.Bot):
    bot.add_cog(Help(bot))