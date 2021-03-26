from discord.ext import commands
from .handlers.jokes import joke_handler
from .handlers.reddit import reddit_handler
class FunnyCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.jokeHandler = joke_handler.JokeHandler()
    self.redditHandler = reddit_handler.RedditHandler()
  
  @commands.command() 
  async def joke(self, ctx, *args):
    async with ctx.typing():
      if len(args)>0:
        category = args[0]
      else:
        category = joke_handler.JokeHandler.jokeCategory[0]
      response = await self.jokeHandler.get_joke(category)
    await ctx.send(response)

  @commands.command()
  async def meme(self, ctx):
    async with ctx.typing():
      response = await self.redditHandler.get_meme()
    await ctx.send(response)

def setup(bot):
  bot.add_cog(FunnyCommands(bot))

 