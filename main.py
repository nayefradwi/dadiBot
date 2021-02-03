import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from commands import message_handler as mh
from commands import funny_commands, cute_commands, dev_commands

# env variables
dadi = os.getenv('dadi')

# setting up commands
bot = commands.Bot(command_prefix="dadi ")
funny_commands.setup(bot)
cute_commands.setup(bot)
dev_commands.setup(bot)

# bot access prefrences
intents = discord.Intents.default()
intents.presences = True
intents.members = True

# printing when the bot is online
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# handling non command messages
@bot.event
async def on_message(nessage):
  response = await mh.handleMessage(nessage, dadi)
  if response == None:
    await bot.process_commands(nessage)

keep_alive()
bot.run(os.getenv('TOKEN'))
