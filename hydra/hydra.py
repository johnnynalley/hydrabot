import os

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
    print('Logged in as ' + bot.user.name)
    print(bot.user.name + '\'s user ID is ' + str(bot.user.id) + '.')
    print('----------')


@bot.event
async def on_member_join(member):
    print(member.name + ' has joined the server. Sending welcome message now...')
    await member.send(welcomeMessage)
    print("Sent welcome message to " + member.name + '.')


load_dotenv()
bot.run(os.getenv('TOKEN'))
