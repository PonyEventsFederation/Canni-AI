import discord

class MessageHandler:
    client: discord.Client = None
    def __init__(self, discordClient: discord.Client):
        self.client = discordClient

    async def MessageRecieved(self, message: discord.Message):
        if message.content.startswith("!hello"):
            msg = 'Hello {0.author.mention}'.format(message)
            await message.channel.send(msg)