import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from settings import (
    welcomeMessage,
    intents,
    command_prefix,
    description
)

bot = commands.Bot(command_prefix=command_prefix, description=description, intents=intents)


# Prints message in terminal when the bot is started
@bot.event
async def on_ready():
    print(f'{bot.user.name} has started.')
    print(f"{bot.user.name}'s user ID is {bot.user.id}.")
    print('----------')


@bot.event
async def on_member_join(member):
    print()
    print(f'{member.name} has joined the server. Sending welcome message now...')
    await member.send(welcomeMessage)
    print(f"Sent welcome message to {member.name}.")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    print()
    await member.kick(reason=reason)
    print(f'User {ctx.author} used the kick command on {member.name}.')
    print(f'Kicking {member.name} from the server...')
    await ctx.channel.send(f"**{member.name}** has been kicked from the server by **{ctx.author}**.")
    print(f'{member.name} has been kicked from the server.')


load_dotenv()
bot.run(os.getenv('TOKEN'))
