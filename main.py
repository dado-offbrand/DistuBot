from keep_alive import keep_alive

import commands
import discord
import json
import os

#-----------------------------------------------#
# BOT INIT (external, has internal ref.)
#-----------------------------------------------#

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#-----------------------------------------------#
# BOT HANDLER
#-----------------------------------------------#

class DistuBotHandler:
  def __init__(self):
    super().__init__()
    file = open('tok.json')

    self.client = client
    self.jdata = json.load(file)
    self.cmds = commands.CommandHandler()
    self.prefix = "~d"
    
#-----------------------------------------------#
# BOT EVENTS
#-----------------------------------------------#

@client.event
async def on_ready():
  print(f'Logged in as {bot.client.user}')

@client.event
async def on_message(message):
  if message.author == bot.client.user:
    return

  cmd_type = bot.cmds.det_cmd_type(message)
  msg = ''
  ebd = False

  if cmd_type == bot.cmds.cmd_types[0]:
    msg = bot.cmds.cmd_from_msg(message)

    if type(msg) == discord.Embed:
      ebd = True
  elif cmd_type == bot.cmds.cmd_types[1]:
    msg = bot.cmds.reaction_from_msg(message)
  else:
    return

  if not ebd:
    await bot.cmds.send_message(message, msg)
    print('sending message')
  else:
    await bot.cmds.send_embed(message, msg)
    print('sending embed')
  
#-----------------------------------------------#
# START BOT, INIT CLASS
#-----------------------------------------------#

if __name__ == "__main__":
  bot = DistuBotHandler()

  keep_alive()
  bot.client.run(bot.jdata["TOKEN"])