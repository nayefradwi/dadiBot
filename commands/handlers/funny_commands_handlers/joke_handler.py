import requests
import sys
jokeApiUrl = 'https://v2.jokeapi.dev/joke/Dark'
jokeType = "type"
single = "single"
setup = "setup"
delivery = "delivery"
joke = "joke"
async def api_request():
  response = requests.get(jokeApiUrl)
  jokeJson = response.json()
  return jokeJson


async def get_joke():
  try:
    jokeJson = await api_request()
    if jokeJson[jokeType] == single:
      return jokeJson[joke]
    else:
      jokeSetup = jokeJson[setup]
      jokeDelivery = jokeJson[delivery]
      output = "{}\n||{}||".format(jokeSetup, jokeDelivery)
      return output
  except:
    e = sys.exc_info()[0]
    print(e.with_traceback())
    return "couldnt load a joke"