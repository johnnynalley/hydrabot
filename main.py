import discord

from client_token import token

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# Before trying to run the bot, make sure your create a file called client_token.py in the same directory as this file, and create a variable called "token" which contains the bot token.
client.run(token)
