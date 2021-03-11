from discord.ext import commands


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


bot.run("ODAxMTIzNDU4NTkwNzAzNjY3.YAcGXA.35wVGttaRH-QPGC13L0Uh_nnxCE")
