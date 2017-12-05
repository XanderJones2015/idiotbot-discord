#idiotbotv1
import os
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='$')

@bot.command(pass_context=True)
async def idiot(ctx, user: discord.Member):
    await bot.say((user.name)+" you idiot")

@bot.command(pass_context=True)
async def idiotm(ctx):
    await bot.say("Michael you idiot")

<<<<<<< HEAD
bot.run("")
=======
bot.command
bot.run("Mzg1OTY0Njk3MTI5NTgyNTky.DQJBKQ.UEICEHQXmqOQ4CAYgMW4pkBbepA")
>>>>>>> 3f59ec1f2cdf2dfa2a37ef6bb1f3da9a29612ab9
