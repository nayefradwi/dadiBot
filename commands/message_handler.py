async def handleMessageFromDadi(message):
  tokens = message.content.split(' ')
  if 'pressure' in message.content or 'pressured' in message.content:
    await message.channel.send("suck my dick")
  elif 'liver' in tokens and 'piece' in tokens:
    try:
      await message.add_reaction('<:dadi:704235688886796379>')
    except:
      await message.add_reaction('\U0001F491')
  else:
    await message.add_reaction("🍆")



async def handleMessage(message, dadi):
  if str(message.author.id) == dadi and 'dadi' not in message.content:
    await handleMessageFromDadi(message)
    return True
  elif message.content == 'dadi':
    await message.channel.send("yes nigga")
    return True
  elif 'dadi' in message.content and "i love you" in message.content.lower():
    await message.channel.send('meow')
    return True
  else:
    return None