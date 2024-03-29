import os
from dotenv import load_dotenv
import discord
import requests
import json
import os.path
import mojimoji
from discordwebhook import Discord as hook
from discord.ext import tasks
from datetime import datetime
import tenkifunction

load_dotenv()
client = discord.Client()

#コマンド実装
#開始処理
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def on_message(message):
    if message.author == client.user:
        print("get")
        return
# next weather
    if message.content.startswith('$nextweather'):
        print(quotex)
        #get
        quote = tenkifunction.get_quote()
        #set enbed
        quotex=discord.Embed(title="明日の天気予報--南部--",description=quote)
        #send
        await message.channel.send(embed=quotex)
#now weather
    if message.content.startswith('$nowweather'):
        quote2 = tenkifunction.get_quote2()
        quotey=discord.Embed(title="今日の天気予報--南部--",description=quote2)
        await message.channel.send(embed=quotey)
    if message.content.startswith('$hei'):
        await message.channel.send("やっほ")

#aleat関係
    #一番大事
#イベント内に関数を配置せずに何とかする

    if message.content.startswith('$aleat '):
        #file path
        base = os.path.dirname(os.path.abspath(__file__))
        #json load
        CITYCODE = json.load(
            open(base + "/aleat.json", "r", encoding="utf-8"))
        #message do
        clasareacode = message.content.replace('$aleat ', '')
        clasareacode = {clasareacode}
        #get data from json
        citycode = [
            CITYCODE["citycodes"][code] for code in clasareacode
        ]
        #data
        citycode = "".join(citycode)
        #get
        warning = tenkifunction.warnings("340000",citycode)
        #send
        if "注意報" in warning and "警報" in warning and "ありません" :
            embedmes = discord.Embed(title= "県内に発令されている警報及び注意報", description= warning, color= 0x1e90ff)
            await message.channel.send(embed=embedmes)
        elif "警報" in warning :
            embedmes = discord.Embed(title="県内に発令されている警報及び注意報", description= warning, color = 0xff0000)
            await message.channel.send(embed=embedmes)
        elif "注意報" in warning :
            embedmes = discord.Embed(title = "県内に発令されている警報及び注意報", description = warning, color = 0xffff00)
            await message.channel.send(embed=embedmes)
        #this is error message
        else :
            await message.channel.send("Error")
    #紛れ込んだ岩国ちゃん
    if message.content.startswith('$aleat岩国'):
        warning = warnings("340000","3520800")
        await message.channel.send(warning)


#pass

client.run(os.getenv('TOKEN'))
