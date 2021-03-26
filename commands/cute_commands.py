from discord.ext import commands
from .handlers.reddit import reddit_handler
class CuteCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.redditHandler = reddit_handler.RedditHandler()
  
  @commands.command()
  async def aww(self, ctx):
    async with ctx.typing():
      response = await self.redditHandler.get_seal()
    await ctx.send(response)
    
  @commands.command()
  async def oni(self, ctx):
    await ctx.send("onii-chan")

def setup(bot):
  bot.add_cog(CuteCommands(bot))