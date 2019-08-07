import discord
from Handlers.Commands.Command import CommandBase, CommandType
from Handlers.Commands.BizaamCommand import BizaamCommand

class MessageHandler(object):
    client: discord.Client = None
    def __init__(self, discordClient: discord.Client):
        MessageHandler.client = discordClient

    async def MessageRecieved(self, message: discord.Message):
        for sc in CommandBase.__subclasses__():
            if sc.checkMatch(sc, message):
                if sc.checkCooldown(sc, message.channel) == False:
                    sc.setCooldown(sc, message.channel)
                    await sc.sendMessage(sc, message, MessageHandler.client)
                else:
                    await message.channel.send("Pff I'm still cooling down")