import discord

tokenFile = open("TOKEN_FILE", 'r')
TOKEN = tokenFile.read().rstrip('\n')
tokenFile.close()

client = discord.Client()

def getRecommendation(inputData):
    strResult = "올바르지 않은 입력입니다. 음식점, 주점, 카페 검색만 지원합니다."

    if inputData == "음식점":
        strResult = "음식점 추천 결과입니다."
    elif inputData == "주점":
        strResult = "주점 추천 결과입니다."
    elif inputData == "카페":
        strResult = "카페 추천 결과입니다."
    
    return strResult

def getRoute(inputData):
    locationFrom = inputData.split("~")[0]
    locationTo = inputData.split("~")[1]

    return "Route from %s to %s"%(locationFrom, locationTo)

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
        strResult = getRoute(message.content.split()[1])
        await message.channel.send(strResult)
    elif message.content.startswith('/도움말'):
        await message.channel.send("도움말 메뉴")
    elif message.content.startswith('/주변시설'):
        strResult = getRecommendation(message.content.split()[1])
        await message.channel.send(strResult)

client.run(TOKEN)