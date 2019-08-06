import yaml
import discord
from Handlers.MessageEventHandler import MessageHandler

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
async def on_message(message):
    await msgHandler.MessageRecieved(message)

client.run(cfg['discord_secret_token'])