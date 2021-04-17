import os
import discord
import random
from keep_alive import keep_alive

options = ["scissors", "paper", "rock"]
user_score = 0
bot_score = 0
status = True

client = discord.Client()

def botChoose():
    choice = random.randint(0, len(options)-1)
    return options[choice]


@client.event
async def on_ready():
  print ('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  global bot_score
  global user_score
  global status

  if message.author == client.user:
    return

  if message.content.startswith('$play'):
    status = True
    await message.channel.send('Welcome! Lets play a game of stone paper scissors!')

  if message.content.startswith('$bye'):
    status = False
    await message.channel.send('Okay, Bye!')

  if status:
    if message.content.startswith('$rock'):
      bot = botChoose()
      
      await message.channel.send(bot)
      if bot == 'rock':
        await message.channel.send('We engage with \u26F0') 
      if bot == 'paper':
        bot_score = bot_score+1
        await message.channel.send('I won with \U0001F4F0')
      if bot == 'scissors':
        user_score = user_score + 1
        msg = 'Congrats {0.author.mention}, you won with \u26F0'.format(message)
        await message.channel.send(msg)


    if message.content.startswith('$paper'):
      bot = botChoose()
      await message.channel.send(bot)
      if bot == 'paper':
        await message.channel.send('We engage with \U0001F4F0') 
      if bot == 'scissors':
        bot_score = bot_score+1
        await message.channel.send('I won with \u2702')
      if bot == 'rock':
        user_score = user_score + 1
        msg = 'Congrats {0.author.mention}, you won with \U0001F4F0'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('$scissors'):
      bot = botChoose()
      await message.channel.send(bot)
      if bot == 'scissors':
        await message.channel.send('We engage with \u2702') 
      if bot == 'rock':
        bot_score = bot_score+1
        await message.channel.send('I won with \u26F0')
      if bot == 'paper':
        user_score = user_score + 1
        msg = 'Congrats {0.author.mention}, you won with \u2702'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('$scoreboard'):
      scoreboard = f'{message.author.mention} ---> {user_score}' + '\n' + f'RockPaperScissor Bot ---> {bot_score}' 
      await message.channel.send(scoreboard) 

keep_alive()
client.run(os.environ['TOKEN'])
