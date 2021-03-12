import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

command_prefix = '$'
description = f'''Hydra Commands
Hydra's command prefix is "{command_prefix}"
'''

# bot = commands.Bot(command_prefix=command_prefix, description=description)
bot = commands.Bot(command_prefix=command_prefix, description=description)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'{bot.user.name}\'s user ID is {bot.user.id}')
    print('----------')


bot.run(os.getenv('TOKEN'))
