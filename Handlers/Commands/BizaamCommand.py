import discord
from Handlers.Commands.Command import CommandBase, CommandType

class BizaamCommand(CommandBase):
    def __init__(self):
        self.commandType: CommandType = CommandType.CONTAINS
        self.commandText: str = "Bizaam"
        self.cooldownTimeInSeconds: int = 60
        self.bizaamEmoji: discord.Emoji = None

    async def sendMessage(self, message: discord.Message, client: discord.Client) -> bool:
        await message.add_reaction(self.getBizaamEmoji(client))
        newMessage = await message.channel.send("{0} BIIZAAAAAMM!!!".format(self.getBizaamEmoji(client)))
        await newMessage.add_reaction(self.getBizaamEmoji(client))

    def getBizaamEmoji(self, client: discord.Client):
        if self.bizaamEmoji != None:
            return self.bizaamEmoji
        for emoji in client.emojis:
            if emoji.name.lower() == "bizaam":
                self.bizaamEmoji = emoji
        if self.bizaamEmoji == None:
            return ""
        return self.bizaamEmoji