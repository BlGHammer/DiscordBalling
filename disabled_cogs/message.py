import discord
from discord.ext import commands
import re


async def get_int_list(input: str) -> list[int]:
    return [int(s) for s in re.findall(r'\b\d+\b', input)]
# CallId is [-1]
# CallerUserId is [-2]
# topic: "_____", Caller: <@___>, CallId: ___
# Receive incoming calls, topic: "_____"

async def get_topic_name(input: str) -> str | None:
    startIndex = temp.find('\"')
    if startIndex != -1: #i.e. if the first quote was found
        endIndex = temp.find('\"', startIndex + 1)
        if endIndex != -1: #i.e. both quotes were found
            return input[startIndex+1:endIndex]
# str.lower(channel.Topic[:22]) == "receive incoming calls"


async def can_dm_user(user: discord.User) -> bool:
    ch = user.dm_channel
    if ch is None:
        ch = await user.create_dm()

    try:
        await ch.send()
    except discord.Forbidden:
        return False
    except discord.HTTPException:
        return True

async def get_user_channel(user: discord.user, bot) -> discord.channel:
    print("Getting channel...")
    guild: discord.guild = bot.get_guild(1071040249477730356)
    print(len(guild.categories))
    category = discord.utils.get(guild.categories, name="tickets") #discord.utils.get(guild.categories, id=1071123470248845332)
    if category: 
        print("Category found!")
        channel = discord.utils.get(category.channels, name= f"ticket-{user.id}")
        if not channel:
            print("No channel found, creating channel")
            channel = False # create channel under the category
            # on user dm create channel
            # on channel message send it to the player
            channel = await category.create_text_channel(f'ticket-{user.id}')
        return channel

class Message(commands.Cog, name = "Message"):
    """Receives message commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot 
    
    @commands.slash_command()
    async def message(
        self, 
        ctx: commands.Context, 
        user: discord.Option(discord.User, "Insert a user!"), 
        *, msg
    ):
        """Send a direct message!"""
        if await can_dm_user(user): #user.can_send()
            print("Can send!")
            #channel = user.creat_dm()
            #print("Has channel!")
            await user.send(msg)
            await ctx.respond(f"`Responded with: {Message}`")
            return
        
        await ctx.respond("`ERROR: Can't send DM`")

    @commands.Cog.listener()
    async def on_message(self, message : discord.message):
        print("Message detected!")
        msg = message.content
        if message.author.id == self.bot.user.id: 
            return
        if isinstance(message.channel, discord.DMChannel): #in dm channel
            print("It was a DM message")
            channelToMsg: discord.channel = await get_user_channel(message.author, self.bot)
            await channelToMsg.send(msg)
            # send message to channel^
            return
        if message.channel.category.name == "tickets":
            print("It was a ticket message")
            # server channel
            #await message.author.send("message")
            userId = message.channel.name.split("-")[-1]
            guild = await self.bot.fetch_guild(1071040249477730356)
            member: discord.Member = await guild.fetch_member(userId) # might error pls fix
            print(f"\'{msg}\'")
            if member and await can_dm_user(member): #user.can_send()
                # if msg is "" then send back an error to channel which the msg came from or reply to the user
                await member.send(msg)
                return


      

    
def setup(bot: commands.bot):
    bot.add_cog(Message(bot))