import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
import discord
from discord.ext import commands
import os


BOT_PREFIX=("...............................................................")

client= Bot(command_prefix=BOT_PREFIX)

@client.listen()
async def on_message(message):
    channel = discord.Object(id=os.getenv("Chan"))
    if message.author.bot:
        pass
    elif(message.author.id == os.getenv("Usero")):
        pass
    elif(message.author.id == os.getenv("Usert")):
        pass
    elif(message.author.id == os.getenv("Userth")):
        pass
    elif(message.author.id == os.getenv("Userf")):
        pass
    elif(message.author.id == os.getenv("Userfi")):
        pass
    elif(message.author.id == os.getenv("Usersi")):
        pass
    elif(message.author.id == os.getenv("Userse")):
        pass
    else:
        await client.send_message(channel, '{0} wrote {1} '.format(message.author, message.content))
        

@client.event
async def on_member_join(member):
    await client.send_message(member, "welcome {0} to {1}".format(member, member.server))

client.run(os.getenv("TOKEN"))
