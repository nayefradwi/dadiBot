import requests
import sys
from commands.message_styles import code_block


class JokeHandler():
  jokeApiUrl = 'https://v2.jokeapi.dev/joke/'
  jokeType = "type"
  single = "single"
  setup = "setup"
  delivery = "delivery"
  joke = "joke"
  jokeCategory = ['dark', 'programming']

  async def api_request(self, url):
    response = requests.get(url)
    jokeJson = response.json()
    return jokeJson

  async def handleJoke(self,url):
    try:
      jokeJson = await self.api_request(url)
      if jokeJson[JokeHandler.jokeType] == JokeHandler.single:
       return jokeJson[JokeHandler.joke]
      else:
        jokeSetup = jokeJson[JokeHandler.setup]
        jokeDelivery = jokeJson[JokeHandler.delivery]
        output = "{}\n||{}||".format(jokeSetup, jokeDelivery)
        return output
    except:
      e = sys.exc_info()[0]
      print(e.with_traceback())
      return "couldnt load a joke"

  async def get_joke(self, jokeCategory):
    if jokeCategory.lower() in JokeHandler.jokeCategory:
      return await self.handleJoke(JokeHandler.jokeApiUrl+jokeCategory)
    return code_block.codeBlock("unkown joke category\ntry dark or programming")

    