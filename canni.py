import discord
import configparser
import datetime
import requests
import asyncio
import logging
import os
import json

rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)-19s | %(levelname)-8s | %(name)-16s | %(message)-s', "%d-%m-%Y %H:%M:%S")
consoleHandler.setFormatter(formatter)
consoleHandler.setLevel(logging.DEBUG)
rootLogger.addHandler(consoleHandler)

discordLogger = logging.getLogger("discord") # Prevent discord and websockets from spamming the console
discordLogger.setLevel(logging.WARNING)
websocketLogger = logging.getLogger("websockets")
websocketLogger.setLevel(logging.WARNING)

# Abstract away client events into a class
class DiscordBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Initializing bot")
        if not os.path.exists("./settings/"):
            self.logger.debug("Settings folder was missing, creating it")
            os.mkdir("./settings")
        self.fConfig = os.path.join("./settings", "config.cfg")
        self.fPlaylist = os.path.join("./settings", "playlist.json")

        self.galaconDate = datetime.datetime.strptime("07:00:00 1 8 2020", "%H:%M:%S %d %m %Y") # 9:00 - 2:00 (cuz GMT+2)

        # Load the config
        self.config = Config(self.fConfig)
        self.userToken = self.config.token
        self.prefix = self.config.prefix

        self.youtubeAPI = self.config.youtubeAPI

        self.game = discord.Activity(
            type = discord.ActivityType.playing,
        )
    
    async def on_ready(self):
        self.logger.info("Logged in as {name}".format(name=self.user.name))
        self.loop.create_task(self.updateTime())
    
    async def on_message(self, message):
        if(message.author == self.user or message.author.bot):
            return # return silently
        try:
            if(message.raw_mentions[0] == self.user.id):
                pass # Handle mention things here
        except IndexError:
            pass
        if("bizaam" in message.content.lower()):
            bizaamEmoji = None
            for emoji in message.guild.emojis:
                if(emoji.name.lower() == "bizaam"):
                    bizaamEmoji = emoji
                    break
            if(bizaamEmoji == None):
                return
            await message.add_reaction(bizaamEmoji)
            newMessage = await message.channel.send("{} BIIZAAAAAMM!!!".format(str(bizaamEmoji)))
            await newMessage.add_reaction(bizaamEmoji)
    
    async def updateTime(self):
        timedelta = self.galaconDate - datetime.datetime.utcnow()
        days = timedelta.days
        hours = timedelta.seconds//3600
        minutes = (timedelta.seconds//60)%60
        self.logger.info("Time to Galacon: {days} days, {hours}:{minutes} left! Hype!".format(days=days, hours=hours, minutes=minutes))
        self.game.name="Time to Galacon: {days} days, {hours}:{minutes} left! Hype!".format(days=days, hours=hours, minutes=minutes)
        await self.change_presence(activity=self.game)
        await asyncio.sleep(10)

    def run(self):
        self.logger.info("Logging in")
        if not self.userToken:
            self.logger.critical("Token isn't defined, aborting")
            return
        super().run(self.userToken)

class Config:
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.logger = logging.getLogger(self.__class__.__name__)
        if not os.path.exists(self.file):
            self.reset()
        config = configparser.ConfigParser()
        config.read(self.file, encoding="utf-8")

        self.token = config.get("Auth", "token", fallback="")
        self.logger.debug("Loading Discord token")
        if self.token == "":
            self.token = False
        if not self.token:
            self.logger.critical("Discord bot token is missing in the config, bot won't be able to start!")

        self.logger.debug("Loading Youtube API token")
        self.youtubeAPI = config.get("Administration", "youtubeAPI", fallback="")
        if self.youtubeAPI == "":
            self.youtubeAPI = False
        if not self.youtubeAPI:
            self.logger.warning("Youtube Data API key isn't configured, some functions will be missing")

        self.prefix = config.get("Administration", "prefix", fallback=None)
        if self.prefix == "":
            self.prefix = None
            self.logger.debug("Couldn't find prefix, defaulting to mention on login")
        else:
            self.logger.debug("Prefix set to \"{prefix}\"".format(prefix=self.prefix))
    
    def reset(self):
        config = configparser.ConfigParser(allow_no_value=True)
        self.logger.warning("Resetting config to default values")
        config.add_section("Auth")
        config.set("Auth", "token", "")
        config.add_section("Administration")
        config.set("Administration", "youtubeAPI", "")
        config.set("Administration", "prefix", "")

        with open(self.file, "w", encoding="utf-8") as file:
            config.write(file)

#Start discord Bot
client = DiscordBot()

client.run()