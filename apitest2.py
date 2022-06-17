import os
from dotenv import load_dotenv
import discord
import requests
import json
import os.path
import mojimoji
from discordwebhook import Discord as hook
load_dotenv()

hook = hook(url="https://discord.com/api/webhooks/987346842104791070/60wJv65ac2q3u7-6mVej2zTSVquVFG7cnnRJdL0KQ5RtjK2h0bMBH7hPv7mNqFNYPeKM")
hook.post(
    embeds=[{"title": "Embed Title", "description": "Embed description"}],
)

client = discord.Client()
#今思ったけどなんで日本語でコメント書いてるんだ？　::coment is japanese (頭悪そう)
#気象庁から天気予報をいただくぜ
def get_quote():
    jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json"
    jma_json = requests.get(jma_url).json()

    #取得したいデータを選ぶ
    jma_place = jma_json[0]["publishingOffice"]
    jma_timeget = jma_json[0]["reportDatetime"]
    jma_date = jma_json[0]["timeSeries"][0]["timeDefines"][1]
    jma_temp = jma_json[1]["tempAverage"]["areas"][0]["max"]
    jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][1]
    jma_weather = jma_weather.replace('　', '')
    jma_return = [
        '明日の天気予報--南部--', jma_place, "予報取得時刻  " + jma_timeget,
        "予報時刻  " + jma_date, jma_weather, '最高気温  ' + jma_temp + '℃',
        'データーは気象庁より'
    ]
    return ('\n'.join(jma_return))
#気象庁からその日の天気をいただくぜ
def get_quote2():
    jma_url2 = "https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json"
    jma_json2 = requests.get(jma_url2).json()

    jma_place2=jma_json2[0]["publishingOffice"]
    jma_timeget2=jma_json2[0]["reportDatetime"]
    jma_date2 = jma_json2[0]["timeSeries"][0]["timeDefines"][0]
    jma_temp2=jma_json2[0]["timeSeries"][2]["areas"][0]["temps"][0]
    jma_weather2 = jma_json2[0]["timeSeries"][0]["areas"][0]["weathers"][0]
    jma_weather2 = jma_weather2.replace('　', '')
    jma_return2 = ['今日の天気予報--南部--',jma_place2,"予報取得時刻  "+jma_timeget2,"予報時刻  "+jma_date2,jma_weather2,'最高気温  '+jma_temp2+'℃','データーは気象庁より']
    return ('\n'.join(jma_return2))
#警報をいただくぜ


def warnings(a,b):

    base = os.path.dirname(os.path.abspath(__file__))

    WEATHER_TRANS = json.load(
        open(base + "/transweather.json", "r", encoding="utf-8"))

    OFFICES_AREA_CODE = a
    CLASS_AREA_CODE = b
    AREA_URL = "https://www.jma.go.jp/bosai/common/const/area.json"
    url = "https://www.jma.go.jp/bosai/warning/data/warning/%s.json" % (OFFICES_AREA_CODE)

    area_data = requests.get(AREA_URL).json()
    area = area_data["class20s"][CLASS_AREA_CODE]["name"]
    warning_info = requests.get(url).json()

    warning_codes = [
        warning["code"] for class_area in warning_info["areaTypes"][1]["areas"]
        if class_area["code"] == CLASS_AREA_CODE
        for warning in class_area["warnings"]
        if warning["status"] != "解除" and warning["status"] != "発表警報・注意報はなし"
    ]
    #print (warning_codes)
    warning_texts = [
        WEATHER_TRANS["warninginfo"][code] for code in warning_codes
    ]
    #print (warning_texts)
    if warning_texts == []:
            warning_text = "現在発表されている警報・注意報はありません。"
    else:
            warning_texts ="".join(warning_texts)
            warning_text = warning_texts+"が発表されています"
    warning_return = [area+"では",warning_text]
    return ("".join(warning_return))

#起動確認だよん
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
#コマンド実装
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$nextweather'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('$nowweather'):
        quote2 = get_quote2()
        await message.channel.send(quote2)
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
        print(clasareacode)
        citycode = [
            CITYCODE["citycodes"][code] for code in clasareacode
        ]

        print(clasareacode)
        print(citycode)
        citycode = "".join(citycode)
        warning = warnings("340000",citycode)
        await message.channel.send(warning)
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


#pass

client.run(os.getenv('TOKEN'))
