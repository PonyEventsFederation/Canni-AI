import discord
from Handlers.Commands.Command import CommandBase, CommandType
from Handlers.Commands.BizaamCommand import BizaamCommand
from Handlers.Commands.ILoveYouCommand import ILoveYouCommand

class MessageHandler():
    def __init__(self, discordClient: discord.Client):
        self.client = discordClient

    async def MessageReceived(self, message: discord.Message):
        for sc in CommandBase.__subclasses__():
            if sc.checkMatch(sc, message):
                if sc.checkCooldown(sc, message.channel) == False:
                    sc.setCooldown(sc, message.channel)
                    await sc.sendMessage(sc, message, self.client)
                else:
                    await message.channel.send("Pff I'm still cooling down")