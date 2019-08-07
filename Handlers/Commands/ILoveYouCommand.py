import discord
from Handlers.Commands.Command import CommandBase, CommandType

class ILoveYouCommand(CommandBase):
    commandType: CommandType = CommandType.CONTAINS
    commandText: str = "I love you"
    cooldownTimeInSeconds: int = 60
    cooldownChannels = []
    loveEmoji: discord.Emoji = None

    async def sendMessage(self, message: discord.Message, client: discord.Client) -> bool:
        if message.raw_mentions:
            if message.raw_mentions[0] == client.user.id:
                await message.channel.send("<@{0}> I love you too! {1}".format(message.author.id, self.getLoveEmoji(client)))

    @staticmethod
    def getLoveEmoji(client: discord.Client):
        if ILoveYouCommand.loveEmoji != None:
            return ILoveYouCommand.loveEmoji
        for emoji in client.emojis:
            if emoji.name.lower() == "love":
                ILoveYouCommand.loveEmoji = emoji
        if ILoveYouCommand.loveEmoji == None:
            return "🤗"
        return ILoveYouCommand.loveEmoji