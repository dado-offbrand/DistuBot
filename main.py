# -- <<< Imports >>> -- #
import discord
import os

from keep_alive import keep_alive
from return_cursed import return_cursed_fact
from return_cursed import return_cursed_img
client = discord.Client()

# -- <<< Variables >>> -- #
prefix = "~d"

# When the bot starts up
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

# -- <<< Main Program >>> -- #
@client.event
async def on_message(message):
  # Ignoring itself
  if message.author == client.user:
    return

  # -- <<< Commands >>> -- #
  if '~d' in message.content:
    # Gives random cursed image
    if 'cursed image' in message.content:
      await message.channel.send(return_cursed_img())
  
    # Greet command
    if 'hello' in message.content:
      await message.channel.send("hello, whats up qt?")

    # Random cursed fact command
    if 'cursed fact' in message.content:
      await message.channel.send(return_cursed_fact())
 
    # Help command
    if 'help' in message.content:
      embed=discord.Embed(title="Command help", description="Basic descriptions of commands.", color=0xffffff)
      embed.set_author(name="DistuBot Help")
      embed.add_field(name="~d cursed fact", value="Gives a random cursed fact.", inline=False)
      embed.add_field(name="~d cursed image", value="Gives a random cursed image.", inline=False)
      embed.add_field(name="~d fact", value="Gives a fact.", inline=False)
      embed.add_field(name="~d hello", value="Greets you!", inline=False)
      embed.add_field(name="~d chirp", value="Chirp..!", inline=False)
      embed.add_field(name="~d repeat", value="Make the bot repeat your message", inline=False)
      embed.set_footer(text="If you need more help, DistuBot is probably not for you! It's a personal bot anyways.")
      await message.channel.send(embed=embed)

    # Chirp command
    if 'chirp' in message.content:
      await message.channel.send("https://cdn.discordapp.com/attachments/798363867482423298/853517850705526784/video0-12.mp4")

    # Mock command
    if 'repeat' in message.content:
      mockedMessage = message.content
      mockedMessage = mockedMessage.strip("~d repeat")
      await message.channel.purge(limit=1)
      await message.channel.send(mockedMessage)

# -- <<< Run Bot >>> -- #
keep_alive()
client.run(os.getenv('TOKEN'))
