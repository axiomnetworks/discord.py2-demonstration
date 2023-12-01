import discord, os, asyncio
from discord.ext import commands

intents = discord.Intents.all()

prefix = ["prefix!", "PREFIX!"] # edit the prefix to whatever you'd like

client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="the demonstration")) # you may edit the status
    print("Logged in!")

@client.command()
async def sync(ctx) -> None:
    try:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"Synced {len(fmt)} commands.")
    except Exception as e:
        print(e)

async def load():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                print(f"Attempting to load {file[:-3]}")
                await client.load_extension(f"cogs.{file[:-3]}")
            except Exception as e:
                print(f"Failed to load extension {file[:-3]}")
                print(e)

async def main():
    await load()
    await client.start("INSERT BOT TOKEN")

asyncio.run(main())