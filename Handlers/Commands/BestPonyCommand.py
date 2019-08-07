import discord
from Handlers.Commands.Command import CommandBase, CommandType
from Utils.ContentCheck import StrContains

class BestPonyCommand(CommandBase):
    commandType: CommandType = CommandType.CONTAINS
    commandText: str = " is best pony"
    cooldownTimeInSeconds: int = 60
    cooldownChannels = []
    bizaamEmoji: discord.Emoji = None

    async def sendMessage(self, message: discord.Message, client: discord.Client) -> bool:
        if StrContains(message.content, "who is best pony"):
            await message.channel.send("<@{0}> {1} I am, of course!".format(message.author.id, BestPonyCommand.getBizaamEmoji(client)))
        elif StrContains(message.content, "canni is best pony") or StrContains(message.content, "canni soda is best pony"):
            await message.channel.send("<@{0}> I sure am!".format(message.author.id))
        elif StrContains(message.content, "bizaam is best pony"):
            await message.channel.send("<@{0}> A bizaam isn't a pony, silly...".format(message.author.id))
        elif StrContains(message.content, "assfart is best pony"):
            await message.channel.send("<@{0}> Rude!".format(message.author.id))
        else:
            await message.channel.send("<@{0}> Nu-uh. I am best pony!".format(message.author.id))
    
    @staticmethod
    def getBizaamEmoji(client: discord.Client):
        if BestPonyCommand.bizaamEmoji != None:
            return BestPonyCommand.bizaamEmoji
        for emoji in client.emojis:
            if emoji.name.lower() == "bizaam":
                BestPonyCommand.bizaamEmoji = emoji
        if BestPonyCommand.bizaamEmoji == None:
            return ""
        return BestPonyCommand.bizaamEmoji