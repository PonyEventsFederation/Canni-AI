import discord
import abc
from Utils.ContentCheck import StrContains, StrContainsWord, StrStartWith
from enum import Enum

class CommandBase(object):
    __metaclass__ = abc.ABCMeta
    @property
    @abc.abstractmethod
    def commandType(self):
        return NotImplementedError

    @property
    @abc.abstractmethod
    def commandText(self):
        return NotImplementedError

    @abc.abstractmethod
    async def sendMessage(self, message: discord.Message) -> bool:
        return
        
    def checkMatch(self, message: discord.Message) -> bool:
        if self.commandType == CommandType.CONTAINS:
            return StrContains(message.content, self.commandText)
        elif self.commandType == CommandType.CONTAINSWORD:
            return StrContainsWord(message.content, self.commandText)
        else:
            return StrStartWith(message.content, self.commandText)
    pass


class CommandType(Enum):
    STARTSWIDTH = 0
    CONTAINS = 1
    CONTAINSWORD = 2