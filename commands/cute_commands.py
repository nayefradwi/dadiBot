from discord.ext import commands
from .handlers.cute_commands_handlers import seal_image_handler
class CuteCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def aww(self, ctx):
    response = await seal_image_handler.get_seal()
    await ctx.send("under construction")
    
  @commands.command()
  async def oni(self, ctx):
    await ctx.send("onii-chan")

def setup(bot):
  bot.add_cog(CuteCommands(bot))