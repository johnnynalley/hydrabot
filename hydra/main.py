import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from settings import (
    welcomeChannel,
    intents,
    command_prefix,
    description
)

bot = commands.Bot(command_prefix=command_prefix, description=description, intents=intents)


# Prints message in terminal when the bot is started
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'{bot.user.name}\'s user ID is {bot.user.id}')
    print('----------')


# Welcomes new members to the server
@bot.event
async def on_member_join(member):
    print(f"{member.name} has joined the server. Attempting to send welcome message...")
    await bot.get_channel(welcomeChannel).send(f'Welcome to Code with Us, {member.name}!')
    print(f'Sent welcome message to {member.name}.')


# Kick command
@bot.command
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send('Unable to kick yourself.')
        return
    else:
        await member.kick(reason=reason)
        await ctx.send(f'{member} was kicked.')


load_dotenv()
bot.run(os.getenv('TOKEN'))
