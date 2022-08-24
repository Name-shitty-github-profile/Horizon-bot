from nextcord.ext import commands
from nextcord import Intents
bot = commands.Bot(command_prefix=['?'], intents=Intents.all(), help_command=None)
from os import listdir, system, environ
for fn in listdir('cogs'):
  if fn.endswith(".py"):
    bot.load_extension(f'cogs.{fn[:-3]}')
bot.run(environ['token'])
