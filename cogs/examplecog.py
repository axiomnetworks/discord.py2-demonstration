import discord, traceback
from discord.ext import commands
from discord import app_commands

class ExampleCog(commands.Cog):

    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="yourcommandname", description="Your commands description")
    async def yourcommandname(self, interaction : discord.Interaction, exampleargument : str):
        await interaction.response.send_message(exampleargument)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExampleCog(bot), guilds=[discord.Object(id=0)]) # edit the ID to be your servers ID
    print("ExampleCog Loaded\n---")