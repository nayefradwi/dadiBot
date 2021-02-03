from discord.ext import commands
from .handlers.funny_commands_handlers import joke_handler

class FunnyCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(help="something you are too stupid to understand....\n nigha just type 'dadi joke' and I will tell you a joke") 
  async def joke(self, ctx):
      response = await joke_handler.get_joke()
      await ctx.send(response)

def setup(bot):
  bot.add_cog(FunnyCommands(bot))

 