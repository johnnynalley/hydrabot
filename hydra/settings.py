import discord

# Bot intents settings
intents = discord.Intents.default()
intents.members = True

# Command prefix
command_prefix = '$'

# Bot help page
description = f'''Hydra Commands
Hydra's command prefix is "{command_prefix}"
'''

# Welcome message
welcomeMessage = '''
**Welcome to Code with Us!**
Code with Us is a programming community focused on coding, but we also have things that may be of interest to those who do not code.

We have numerous channels for many different programming languages where you can look for help and discuss that language in. In the pinned messages of those channels, we have tips and tricks for programming with that language and resources for learning that language for those who don't already know it.

We also have a custom bot named Hydra, built by LiterallyJohnny, the owner of this server. It is still in development, so don't expect too much from it.
You can find the commands for Hydra by typing `$help` in <#819624945725210645>.
'''
