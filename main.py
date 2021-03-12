import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from variables import welcomeMessage

load_dotenv()

command_prefix = '$'
description = f'''Hydra Commands
Hydra's command prefix is "{command_prefix}"
'''

intents = discord.Intents(members=True)
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
    try:
        await bot.send_message(member, welcomeMessage)
        print(f'Sent welcome message to {member.name}')
    except:
        print(f"Couldn't send welcome message {member.name}.")


bot.run(os.getenv('TOKEN'))
