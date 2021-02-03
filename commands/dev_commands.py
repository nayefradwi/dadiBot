from discord.ext import commands
class DevCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def update(self, ctx):
    f = open("updateLog.txt")
    log = f.read()
    log = log.split(';')
    await ctx.send("@here\n```{}```".format(log[0]))


def setup(bot):
  bot.add_cog(DevCommands(bot))
