import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import typing

intents = discord.Intents.default()
intents.members = True
load_dotenv()
prefix = '$'
bot = commands.Bot(command_prefix=prefix, intents=intents, description='Bot created to shuffle and pick from lists of items or lists of users')


class Source(commands.Converter):
    '''
    Converter to convert an audio of other methods to something that we can shuffle or pick from
    '''
    async def convert(self, ctx, argument):
        if argument in ('audio', 'list'):
            return argument
        raise BadArgument()


@bot.command()
async def shuffle(ctx, arg: typing.Optional[Source] = 'audio', *args):
    '''
    Shuffle and print list of items.

    Usage: 
    'shuffle audio' to shuffle the members of the audio channel you're currently in.
    'shuffle list item1 item2 item3' to shuffle items in list.

    Options: -dm to send the result to your dms.
    '''
    user = ctx.author
    sendTo = ctx
    args = list(args)
    if '-dm' in args:
        sendTo = user
        args.remove('-dm')
    if arg == 'audio':
        # these can't be used in dms
        if ctx.guild == None:
            await sendTo.send("This only works in a server's channel")
            return

        # get audio channel the user is in
        if user.voice != None:
            await sendTo.send('Shuffling members in ' + user.voice.channel.name + '...')
            # get list of members, shuffle it and send it
            channelMembers = user.voice.channel.members
            items = [member.name for member in channelMembers]
            await shuffleAndSend(items, sendTo)
        else:
            await sendTo.send(user.name + " isn't in any audio channel!")
    if arg == 'list':
        items = args
        if len(items) > 0:
            await sendTo.send('Shuffling items in list...')
            await shuffleAndSend(items, sendTo)
        else:
            await sendTo.send("You didn't specify a list to shuffle. Correct usage is `{0}shuffle list item1 item2 item3`".format(prefix))


async def shuffleAndSend(items, sendTo):
    random.shuffle(items)
    for item in items:
        await sendTo.send(item)


@bot.command()
async def pick(ctx, arg: typing.Optional[Source] = 'audio', quantity: typing.Optional[int] = 1, *args):
    '''
    Pick quantity (default 1) from list.

    Usage:
    'pick audio 3' to pick 3 users from the audio channel you're currently in.
    'pick list 2 item1 item2 item3' to pick 2 items from the list (item1, item2, item3).

    Options: -dm to send the result to your dms.
    '''
    user = ctx.author
    sendTo = ctx
    args = list(args)
    if '-dm' in args:
        sendTo = user
        args.remove('-dm')
    if arg == 'audio':
       # get audio channel the user is in
        if (user.voice != None):
            await sendTo.send('Picking members in ' + user.voice.channel.name + '...')
            # get list of members, shuffle it and send it
            channelMembers = user.voice.channel.members
            items = [member.name for member in channelMembers]
            await pickAndSend(items, quantity, sendTo)
        else:
            await sendTo.send(user.name + " isn't in any audio channel!")
    if arg == 'list':
        items = args
        if len(items) > 0:
            await sendTo.send('Picking items in list...')
            await pickAndSend(items, quantity, sendTo)
        else:
            await sendTo.send("You didn't specify a list to pick from. Correct usage is `{0}pick list item1 item2 item3`".format(prefix))


async def pickAndSend(items, quantity, sendTo):
    random.shuffle(items)
    for _ in range(min(quantity, len(items))):
        await sendTo.send(items.pop())


bot.run(os.getenv('TOKEN'))
