import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

intents = discord.Intents.default()
intents.members = True
load_dotenv()
prefix = '$'
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command()
async def shuffle(ctx, arg):
    user = ctx.author
    if arg == 'audio':
        # get audio channel the user is in
        if (user.voice != None):
            await ctx.send('shuffling members in ' + user.voice.channel.name + '...')
            # get list of members, shuffle it and send it
            channelMembers = user.voice.channel.members
            random.shuffle(channelMembers)
            for member in channelMembers:
                await ctx.send(member.name)
        else:
            await ctx.send(user.name + " isn't in any audio channel!")

bot.run(os.getenv('TOKEN'))
