import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

async def load_extensions(bot):
    for cog in os.listdir('./cogs'):
        if cog.endswith(".py"):
            print(cog)
            print(f"cogs.{cog[:-3]}")
            await bot.load_extension(f"cogs.{cog[:-3]}")

async def main(bot):
    @bot.event
    async def on_ready():
        print(f"We have logged in as {bot.user}")

    await load_extensions(bot)

if __name__ == "__main__":
    load_dotenv()
    intents = discord.Intents.all()
    bot = commands.Bot(intents=intents, command_prefix="?")
    asyncio.run(main(bot))
    bot.run(os.getenv("SECRET"))