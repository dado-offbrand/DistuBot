from random import choice
from enum import Enum
import discord
import embeds
import json

class CommandHandler:
    def __init__(self):
        super().__init__()

        file = open('response.json')
        self.jdata = json.load(file)

        self.greetings = self.jdata["greetings"]
        self.reaction_keys = self.jdata["reaction_keys"]
        self.rejections = self.jdata["rejections"]
        self.awk_rejections = self.jdata["awk_rejections"]

        self.embed_presets = embeds.PresetConstructor()
        self.cmd_types = ['traditional', 'reaction', 'none']

    async def send_message(self, dmessage, message):
        await dmessage.channel.send(message)

    async def send_embed(self, dmessage, embed):
        await dmessage.channel.send(embed=embed)

    def cmd_from_msg(self, message):
        cmd = message.content.lower().strip('~d ')
        msg = ''

        match cmd:
            case "chirp":
                msg = ':cricket: *chirp*'

            case 'kill':
                msg = 'this seems illegal and i wont benefit from it..'

            case 'hello':
                msg = choice(self.greetings)

            case 'help':
                msg = self.embed_presets.help_embed()

            case 'hi':
                msg = choice(self.greetings)

            case 'smash':
                msg = choice(self.awk_rejections)

            case _:
                msg = choice(self.rejections)

        return msg

    def reaction_from_msg(self, message):
        cmd = message.content.lower()
        msg = ''

        match cmd:
            case 'disturbing':
                msg = 'who called me?'

            case 'distubot':
                msg = 'who called me?'

            case 'cursed':
                msg = 'did somebody say something to me?'

            case ':D':
                msg = ':D'

        return msg

    def det_cmd_type(self, message):
        if '~d' in message.content.lower():
            return self.cmd_types[0]
        elif message.content.lower() in self.reaction_keys:
            return self.cmd_types[1]
        else:
            return self.cmd_types[2]