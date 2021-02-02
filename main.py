import asyncio
from discord.ext import commands
import discord
import random
import re
from dotenv import load_dotenv
import os
import datetime
from keep_alive import keep_alive

TOKEN = os.getenv('BOT_TOKEN')
PREFIX = '<'
print("Loading bot..")

bot = commands.Bot(command_prefix=PREFIX, self_bot=True)
bot.remove_command("help")

def convert(amount): 
    return str(datetime.timedelta(seconds = amount*7210))

@bot.event
async def on_ready():
    print("Connection secure, bot ready!")

@bot.command()
async def abump(ctx, amount=100):
    if amount == 0:
        print("Please enter a number higher than 0")
    elif amount == 1:
        await ctx.send("!d bump")
        print("Bump complete")
    else:
        print("Bumping for",convert(amount))
        await ctx.send("!d bump")
        for r in range(amount):
            await asyncio.sleep(random.uniform(7200, 7210))
            await ctx.send("!d bump")
        print("Bump complete")

keep_alive()
bot.run(TOKEN, bot=False)