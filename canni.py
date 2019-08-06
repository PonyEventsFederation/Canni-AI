import yaml
import discord
from Handlers.MessageEventHandler import MessageHandler
from Handlers.Commands.Command import CommandBase
from Handlers.Commands.BizaamCommand import BizaamCommand

#Load config
with open("config.yml", 'r') as configYmlfile:
    cfg = yaml.load(configYmlfile, Loader=yaml.FullLoader)

#Start discord Bot
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

msgHandler = MessageHandler(client)
@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    await msgHandler.MessageRecieved(message)

client.run(cfg['discord_secret_token'])