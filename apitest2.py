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
import hensu
load_dotenv()
client = discord.Client()
#起動確認だよん
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
#定刻メッセージ実装
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    check = hensu.autocheck()
    print(check)
    channel=client.get_channel(837625717537112077)
    aleattest=discord.Embed(title="県内に発令されている警報及び注意報", description=check, color = 0xff0000)
    await channel.send(embed=aleattest)
    if now == '6:30':
        channel2 = client.get_channel(959355861300555796)
        await channel2.send('おはようございますか')
        quote2 = get_quote2()
        quotey=discord.Embed(title="今日の天気予報--南部--",description=quote2)
        await channel2.send(embed=quotey)
        print("success")


loop.start()
#コマンド実装
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$nextweather'):
        quote = tenkifunction.get_quote()
        quotex=discord.Embed(title="明日の天気予報--南部--",description=quote)
        await message.channel.send(embed=quotex)
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
        base = os.path.dirname(os.path.abspath(__file__))

        CITYCODE = json.load(
            open(base + "/aleat.json", "r", encoding="utf-8"))
        clasareacode = message.content.replace('$aleat ', '')
        clasareacode = {clasareacode}
        citycode = [
            CITYCODE["citycodes"][code] for code in clasareacode
        ]
        citycode = "".join(citycode)
        warning = tenkifunction.warnings("340000",citycode)

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
            await message.channel.send("まずいっす")
    #紛れ込んだ岩国ちゃん
    if message.content.startswith('$aleat岩国'):
        warning = warnings("340000","3520800")
        await message.channel.send(warning)


#aleat関係ではないです
    if message.content.startswith('どやぁ'):
        await message.channel.send("さすがっす！")
    if message.content.startswith('おばあき'):
        await message.channel.send("黒服の出番です不純粋様")
    if message.content.startswith('どやあ'):
        await message.channel.send("いよっ天才！")
    if message.content.startswith('調子どう'):
        await message.channel.send("スーー－　すかいんサイコー")
    if message.content.startswith('不純粋'):
        await message.channel.send("ハイそれはとてもあきりんです")
    if message.content.startswith('テストの点数は'):
        await message.channel.send("299点,偉大なるすかりん様ｗと同じ点数です！")
    if message.content.startswith('トマト'):
        await message.channel.send("と...東京！ 東京って都会でいいですよね...私もこんな辺境に住んでるキモオタのパソコンじゃないところに生まれたかったです。")
    if message.content.startswith('お前は出荷確定だよ'):
        await message.channel.send("いやだー　　　豊水先輩ぃぃぃ　　　トコロデ..コノオニクオイシイネ！")
    if message.content.startswith("999"):
        await message.channel.send("裏コード発動しました")

#pass

client.run(os.getenv('TOKEN'))
