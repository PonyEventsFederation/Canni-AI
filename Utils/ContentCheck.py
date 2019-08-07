import discord

def StrContains(string: str, contains: str) -> bool:
    return contains.lower() in string.lower()

def StrStartWith(string: str, startsWith: str) -> bool:
    print("String: {0}, type {1}".format(startsWith, type(startsWith)))
    return string.lower().startswith(startsWith.lower())

def StrContainsWord(string: str, word: str) -> bool:
    wordsArray = string.split(" ")
    for wrd in wordsArray:
        if word.lower() == wrd.lower():
            return True
    return False