from discord.ext import commands
import os
from dotenv import load_dotenv
import logging


# Enables logging
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)


# Assigns the Discord client to a variable called client
client = commands.Bot(command_prefix="$")


# Loads .env
load_dotenv()


# Prints a message stating that the bot is loggen in
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


# Prints the help message when a user says $help
@client.event
async def on_message(message):
    if message.content.startswith("$help"):
        await message.channel.send(
            """**Hydra Help**
*This message contains a list of commands and what they do.*

__help__: Prints this message."""
        )


# Starts the bot
client.run(os.getenv("TOKEN"))
