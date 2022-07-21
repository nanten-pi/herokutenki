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

def autocheck():
    citycode = 3410100
    while True:
        try:
            citycode2 = str(citycode)
            warning = tenkifunction.warnings("340000",citycode2)
            if citycode >= 3500000 :
                print("Breaked!")
                continue
            elif "注意報" in warning and "警報" in warning and "ありません" :
                citycode += 100
                print("green")
                print(warning)
            elif  "警報" in warning :
                print(warning)
                embedmes = discord.Embed(title="県内に発令されている警報及び注意報", description= warning, color = 0xff0000)
                return (embedmes)
                citycode += 100
            else :
                citycode += 100

        except KeyError :
            print("error")
            citycode += 100
autocheck ()
