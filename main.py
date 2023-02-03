import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

def main():
    load_dotenv()
    intents = discord.Intents.all()
    bot = discord.Bot(intents=intents) # = commands.Bot(command_prexif="?")
    
    @bot.event
    async def on_ready():
        print(f"We have logged in as {bot.user}")

    for cog in os.listdir('./cogs'):
        if cog.endswith(".py"):
            print(cog)
            print(f"cogs.{cog[:-3]}")
            bot.load_extension(f"cogs.{cog[:-3]}")

    bot.run(os.getenv("SECRET"))

if __name__ == "__main__":
    main()