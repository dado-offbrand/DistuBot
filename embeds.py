import discord

class PresetConstructor:
    def __init__(self):
        super().__init__()

    def help_embed(self):
        embed=discord.Embed(title='Command help', description='Basic descriptions of commands.', color=0xffffff)
        embed.set_author(name='DistuBot Help')
        embed.add_field(name='~d cursed fact', value='Gives a random cursed fact.', inline=False)
        embed.add_field(name='~d cursed image', value='Gives a random cursed image.', inline=False)
        embed.add_field(name='~d hello', value='Greets you!', inline=False)
        embed.add_field(name='~d chirp', value='Chirp..!', inline=False)
        embed.add_field(name='~d repeat', value='Make the bot repeat your message', inline=False)
        embed.add_field(name='~d kill', value='Who knows what this does..')
        embed.add_field(name='~d purge', value='Purge X amount of messages. Numbers only please', inline=False)
        embed.add_field(name='Chat queues', value='Saying some keywords will make the bot speak (they are secret!)', inline=False)
        embed.set_footer(text='I am a personal bot. I shouldn\'nt be in other servers.')
        return embed

    def img_embed(self):
        a = "b" # placeholder

    def fact_embed(self):
        a = "b" # placeholder