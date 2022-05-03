import discord
import os
import requests
import json
import os.path

client = discord.Client()


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
#!/usr/bin/env python3

base = os.path.dirname(os.path.abspath(__file__))

WEATHER_TRANS = json.load(
    open(base + "/transweather.json", "r", encoding="utf-8"))
OFFICES_AREA_CODE = "340000"  #地方エリアのコード
CLASS_AREA_CODE = "3421200"  #市町村区のコード
AREA_URL = "https://www.jma.go.jp/bosai/common/const/area.json"

url = "https://www.jma.go.jp/bosai/warning/data/warning/%s.json" % (
    OFFICES_AREA_CODE)


def warnings():
    area_data = requests.get(AREA_URL).json()
    area = area_data["class20s"][CLASS_AREA_CODE]["name"]
    warning_info = requests.get(url).json()

    warning_codes = [
        warning["code"] for class_area in warning_info["areaTypes"][1]["areas"]
        if class_area["code"] == CLASS_AREA_CODE
        for warning in class_area["warnings"]
        if warning["status"] != "解除" and warning["status"] != "発表警報・注意報はなし"
    ]
    warning_texts = [
        WEATHER_TRANS["warninginfo"][code] for code in warning_codes
    ]

    return (area, warning_texts)


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
    if message.content.startswith('$aleat'):
        warning = warnings()
        await message.channel.send(warning)


#pass
client.run("OTcwNjA0ODcwMDczNzQ1NDA4.GAGxEo.hp0my7LwrpQTqqIdaTLRar3jDoPfkwXXYzEdE0")
