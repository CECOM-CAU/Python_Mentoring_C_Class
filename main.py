import discord

tokenFile = open("TOKEN_FILE", 'r')
TOKEN = tokenFile.read().rstrip('\n')
tokenFile.close()

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('/길찾기'):
        await message.channel.send(message.content)
    elif message.content.startswith('/장소찾기'):
        await message.channel.send(message.content)

client.run(TOKEN)