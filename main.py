import discord

tokenFile = open("TOKEN_FILE", 'r')
TOKEN = tokenFile.read().rstrip('\n')
tokenFile.close()