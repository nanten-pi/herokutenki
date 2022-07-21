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

            if citycode >= 3500000:
                citycode = 3410100
            elif "警報" in warning and "注意報" in warning and "ありません" in warning :
                citycode += 100
            elif "注意報" in warning:
                await channel.send(warning)

                citycode += 100

            else:
                citycode += 100
            citycode += 100
        except KeyError :
            citycode += 100
