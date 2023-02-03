from discord.ext import commands

class Ping(commands.Cog, name = "Ping"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot 

    @commands.slash_command()
    async def ping(self, ctx: commands.Context):
        """Responds with Pong!"""
        await ctx.respond(f"Pong! `{(self.bot.latency * 1000).__round__()} ms`")
    
def setup(bot: commands.bot):
    bot.add_cog(Ping(bot))