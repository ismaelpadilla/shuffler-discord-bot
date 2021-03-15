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
async def shuffle(ctx, arg, *args):
    '''
    Shuffle and print list of items.
    Usage: 'shuffle audio' to shuffle the members of the audio channel you're currently inf.

    Options: -dm to send the result to your dms.
    '''
    user = ctx.author
    sendTo = ctx
    if '-dm' in args:
        sendTo = user
    if arg == 'audio':
        # get audio channel the user is in
        if (user.voice != None):
            await sendTo.send('Shuffling members in ' + user.voice.channel.name + '...')
            # get list of members, shuffle it and send it
            channelMembers = user.voice.channel.members
            random.shuffle(channelMembers)
            for member in channelMembers:
                await sendTo.send(member.name)
        else:
            await sendTo.send(user.name + " isn't in any audio channel!")

bot.run(os.getenv('TOKEN'))
