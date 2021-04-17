import os
import discord
import requests
import json


client = discord.Client()


def get_joke():
  response = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
  json_data = json.loads(response.text)
  joke = json_data['joke']
  return(joke)

@client.event
async def on_ready():
  print ('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Heyyyy!')

  if message.content.startswith('$joke'):
    joke = get_joke()
    await message.channel.send(joke)

    
client.run(os.environ['TOKEN'])
