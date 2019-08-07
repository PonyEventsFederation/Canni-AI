import discord
from Handlers.Commands.Command import CommandBase, CommandType

class BizaamCommand(CommandBase):
    commandType: CommandType = CommandType.CONTAINS
    commandText: str = "Bizaam"
    cooldownTimeInSeconds: int = 60
    cooldownChannels = []
    bizaamEmoji: discord.Emoji = None


    async def sendMessage(self, message: discord.Message, client: discord.Client) -> bool:
        await message.add_reaction(BizaamCommand.getBizaamEmoji(client))
        newMessage = await message.channel.send("{0} BIIZAAAAAMM!!!".format(BizaamCommand.getBizaamEmoji(client)))
        await newMessage.add_reaction(BizaamCommand.getBizaamEmoji(client))

    @staticmethod
    def getBizaamEmoji(client: discord.Client):
        if BizaamCommand.bizaamEmoji != None:
            return BizaamCommand.bizaamEmoji
        for emoji in client.emojis:
            if emoji.name.lower() == "bizaam":
                BizaamCommand.bizaamEmoji = emoji
        if BizaamCommand.bizaamEmoji == None:
            return ""
        return BizaamCommand.bizaamEmoji