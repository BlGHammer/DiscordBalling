import discord
import os
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[1071040249477730356])
async def ping(ctx):
    await ctx.respond("Pong!")

bot.run(os.getenv("SECRET"))
