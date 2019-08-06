import discord
from Handlers.Commands.Command import CommandBase, CommandType
from Handlers.Commands.BizaamCommand import BizaamCommand

class MessageHandler:
    client: discord.Client = None
    def __init__(self, discordClient: discord.Client):
        self.client = discordClient

    async def MessageRecieved(self, message: discord.Message):
        for sc in CommandBase.__subclasses__():
            if sc.checkMatch(sc, message):
                await sc.sendMessage(sc, message)