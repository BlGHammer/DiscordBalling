import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog, name = "Ping"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot 

    @app_commands.command()
    async def ping(self, interaction: discord.Interaction):
        """Responds with Pong!"""
        await interaction.response.send_message(f"Pong! `{(self.bot.latency * 1000).__round__()} ms`")
    
async def setup(bot: commands.bot):
    await bot.add_cog(Ping(bot))