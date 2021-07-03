import discord
import webbrowser as web

import Recommendation

tokenFile = open("TOKEN_FILE", 'r')
TOKEN = tokenFile.read().rstrip('\n')
tokenFile.close()

client = discord.Client()

def getRecommendation(where, type):
    dataRecommend = Recommendation.getResult(where, type)

    return dataRecommend

def getRoute(inputData):
    urldict = {'정문101관': 'https://han.gl/CfGKk', '정문 102관': 'https://han.gl/JEpsD', '정문 103관': 'https://han.gl/j6VJg',
    '정문 104관': 'https://han.gl/XStr9', '정문 105관': 'https://han.gl/yQCJW', '정문 106관': 'https://han.gl/Z7ijO',
    '정문 107관': 'https://han.gl/jE1xx', '정문 201관': 'https://han.gl/QwaN0', '정문 202관': 'https://han.gl/StIrf',
    '정문 203관': 'https://han.gl/nzh1c', '정문 204관': 'https://han.gl/fazVz', '정문 207관': 'https://han.gl/IOXEw',
    '정문 208관': 'https://han.gl/6T52I', '정문 209관': 'https://han.gl/AkU6d', '정문 301관': 'https://han.gl/7uPiU',
    '정문 302관': 'https://han.gl/0h8Go', '정문 303관': 'https://han.gl/v6J0v', '정문 304관': 'https://han.gl/Ve950',
    '정문 305관': 'https://han.gl/UtoV9', '정문 307관': 'https://han.gl/9ey7m', '정문 308관': 'https://han.gl/dexgZ',
    '정문 309관': 'https://han.gl/kLEzX', '정문 310관':'https://han.gl/hvuGQ',

    '중문 101관': 'http://kko.to/2XMaWDpfM', '중문 102관': 'http://kko.to/tIRqWYp4p', '중문 103관': 'http://kko.to/b8UviDpfB',
    '중문 104관': 'http://kko.to/L1idiDM4p', '중문 105관': 'http://kko.to/KSxAWYpfp', '중문 106관': 'http://kko.to/4PoIWYM4o',
    '중문 107관': 'http://kko.to/_DKIWDM4o', '중문 201관': 'http://kko.to/vqUJWDp4M', '중문 202관': 'http://kko.to/aNZ_iYMfB',
    '중문 203관': 'http://kko.to/3OI_iDMfp', '중문 204관': 'http://kko.to/X1a6iYp4p', '중문 207관': 'http://kko.to/yOUwiYp4p',
    '중문 208관': 'http://kko.to/j-rQWDpfM', '중문 209관': 'http://kko.to/xzR1WDMfM', '중문 301관': 'http://kko.to/HH7LiDp4B',
    '중문 302관': 'http://kko.to/fgtyWYM4B', '중문 303관': 'http://kko.to/myKyiYpfp', '중문 304관': 'http://kko.to/U3gkiYM4o',
    '중문 305관': 'http://kko.to/NYYB3Dp4o', '중문 307관': 'http://kko.to/wW8B3YM4M', '중문 308관': 'http://kko.to/ETTM3Dp4p',
    '중문 309관': 'http://kko.to/Tl5M3Ypfp', '중문 310관': 'http://kko.to/szDHFYM4M',

    '후문 101관': 'https://han.gl/DdHsB', '후문 102관': 'https://han.gl/RaNE6', '후문 103관': 'https://han.gl/nIVQi',
    '후문 104관': 'https://han.gl/1xRGk', '후문 105관': 'https://han.gl/sZyXv', '후문 106관': 'https://han.gl/H7TVw',
    '후문 107관': 'https://han.gl/VPxfC', '후문 201관': 'https://han.gl/KBW1c', '후문 202관': 'https://han.gl/yXhRW',
    '후문 203관': 'https://han.gl/T2dq3', '후문 204관': 'https://han.gl/cqevf', '후문 207관': 'https://han.gl/k6gEo',
    '후문 208관': 'https://han.gl/ssyw1', '후문 209관': 'https://han.gl/wJj6W', '후문 301관': 'https://han.gl/S7QVo',
    '후문 302관': 'https://han.gl/SrKxk', '후문 303관': 'https://han.gl/eomp9', '후문 304관': 'https://han.gl/Hiz9W',
    '후문 305관': 'https://han.gl/1Y6f2', '후문 307관': 'https://han.gl/uR3BN', '후문 308관': 'https://han.gl/01RiH',
    '후문 309관': 'https://han.gl/pPEI3', '후문 310관': 'https://han.gl/DmNf2'}

    locationFrom = inputData.split("~")[0]
    locationTo = inputData.split("~")[1]

    locaionResult = locationFrom + " " + locationTo

    return "%s에서 %s으로 이동하는 최단경로 결과입니다. %s"%(locationFrom, locationTo, urldict[locaionResult])

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
        strResult = "사용법\n /길찾기 [출발지]~[도착지]\n /주변시설 [음식점, 주점, 카페]"
        await message.channel.send(strResult)
    elif message.content.startswith('/주변시설'):
        inputWhere = message.content.split()[1]
        inputType = message.content.split()[2]
        sendData = getRecommendation(inputWhere, inputType)
        sendFile = discord.File(sendData[0])
        sendMessage = sendData[1]
        await message.channel.send(file=sendFile)
        await message.channel.send(sendMessage[0])

client.run(TOKEN)