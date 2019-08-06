import discord
from Handlers.Commands.Command import CommandBase, CommandType

class BizaamCommand(CommandBase):
    commandType: CommandType = CommandType.CONTAINS
    commandText: str = "Bizaam"
    bizaamEmoji: discord.Emoji = None

    async def sendMessage(self, message: discord.Message) -> bool:
        await message.channel.send('BIIZAAAAMMM!!')

    def getBizaamEmoji(self, guild: discord.Guild):
        if self.bizaamEmoji != None:
            return self.bizaamEmoji
        for emoji in guild.emojis:
            if emoji.name.lower() == "bizaam":
                self.bizaamEmoji = emoji
        if self.bizaamEmoji == None:
            return ""