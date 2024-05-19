import discord
import os
import random
from keep_alive import keep_alive
from global_variables import target_id
from images_and_gifs import hug_gifs, stab_gifs


client = discord.Client()

@client.event
# prepare the discord bot
async def on_ready():
  print("We have logged in to discord as {0.user}".format(client))

@client.event
# respond to messages
async def on_message(message):
  # make sure message isn't from bot itself
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('wateringhole help'):
    embeddedHelp = discord.Embed(title='wateringhole help', 
    description='wateringhole bot commands:\n\twateringhole hug (user): hug a user\n\twateringhole stab (user): stab a user\n\thug me: u give a hug to urself')
    await message.channel.send(embed=embeddedHelp)


  if msg.startswith('wateringhole hug'):
    if '<@!' in msg:
      target_id = determine_target_id(msg)
      targetter_id = message.author.id
      action_message = generate_action_message(msg, targetter_id, target_id)
      embeddedHug = prepare_embed(msg, action_message)    
      await message.channel.send(embed=embeddedHug)
    else:
      await message.channel.send("mention someone lol")


  if msg.startswith("wateringhole stab "):
      if '<@!' in msg:
        target_id = determine_target_id(msg)
        targetter_id = message.author.id
        action_message = generate_action_message(msg, targetter_id, target_id)
        embeddedStab = prepare_embed(msg, action_message)
        await message.channel.send(embed=embeddedStab)
      else:
        await message.channel.send("mention somebody lol")


  if "sad" in msg.lower():
    await message.channel.send("stay sad")

  if 'hug me' in msg.lower():
    user_identification = message.author.id

    wateringholeHug = discord.Embed(title='hug', description=f'wateringhole gives <@{user_identification}> a hug')
    wateringholeHug.set_image(url=f'{random.choice(hug_gifs)}')
    await message.channel.send(embed=wateringholeHug)

  if msg.lower() == 'hi':
    if message.author.id == 269202012766339082:
      await message.channel.send("hi wateringhole4")
    elif message.author.id == 743911717125488700:
      await message.channel.send("hi bestie")
    else:
      random_person = message.author.name
      await message.channel.send(f"who R u {random_person}") 

def determine_target_id(msg):
  if msg.startswith('wateringhole stab'):
    target_id = msg.replace('>', '')
    target_id = target_id.replace('wateringhole stab <@!', '')
  elif msg.startswith('wateringhole hug'):
    target_id = msg.replace('wateringhole hug <@!', '')
    target_id = target_id.replace('>', '')
  
  return target_id

def generate_action_message(msg, targetter_id, target_id):
  if msg.startswith('wateringhole stab'):
    message = f"<@{targetter_id}> stabbed <@{target_id}>."
  elif msg.startswith('wateringhole hug'):
    message = f"<@{targetter_id}> gives <@{target_id}> a big hug."

  return message

def prepare_embed(msg, action_message):
  if msg.startswith('wateringhole stab'):
    embeddedAction = discord.Embed(title='stab', description=action_message)
    embeddedAction.set_image(url=f'{random.choice(stab_gifs)}')
  elif msg.startswith('wateringhole hug'):
    embeddedAction = discord.Embed(title='hug', description=action_message)
    embeddedAction.set_image(url=f'{random.choice(hug_gifs)}')

  return embeddedAction



keep_alive()

client.run(os.getenv("TOKEN"))
