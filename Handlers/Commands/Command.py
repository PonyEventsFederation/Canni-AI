import discord
import abc
from Utils.ContentCheck import StrContains, StrContainsWord, StrStartWith
from enum import Enum
import time

class CommandBase():
    def __init__(self):
        self.cooldownChannels = []
    
    __metaclass__ = abc.ABCMeta

    @property
    @abc.abstractmethod
    def commandType(self):
        return NotImplementedError

    @property
    @abc.abstractmethod
    def commandText(self):
        return NotImplementedError

    @property
    @abc.abstractmethod
    def cooldownTimeInSeconds(self):
        return NotImplementedError

    @property
    @abc.abstractmethod
    def cooldownChannels(self):
        return NotImplementedError
    
    @staticmethod
    def checkCooldown(subclass, channel: discord.TextChannel) -> bool:
        for cooldownChannel in subclass.cooldownChannels:
            if cooldownChannel.channel.id == channel.id:
                if cooldownChannel.timestamp + subclass.cooldownTimeInSeconds > time.time():
                    return True
        return False

    @staticmethod
    def setCooldown(subclass, channel: discord.TextChannel):
        subclass.cooldownChannels.append(CooldownChannel(channel, time.time()))

    @abc.abstractmethod
    async def sendMessage(self, message: discord.Message, client: discord.Client) -> bool:
        return
        
    @staticmethod    
    def checkMatch(sc, message: discord.Message) -> bool:
        if sc.commandType == CommandType.CONTAINS:
            return StrContains(message.content, sc.commandText)
        elif sc.commandType == CommandType.CONTAINSWORD:
            return StrContainsWord(message.content, sc.commandText)
        else:
            return StrStartWith(message.content, sc.commandText)
    pass


class CommandType(Enum):
    STARTSWITH = 0
    CONTAINS = 1
    CONTAINSWORD = 2

class CooldownChannel():
    def __init__(self, channel: discord.TextChannel, timestamp: int = 0):
        self.channel = channel
        self.timestamp = timestamp