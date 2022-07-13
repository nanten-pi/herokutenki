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
def autocheck ():
    check = tenkifunction.warnings("340000","3421200")
    check2 = tenkifunction.warnings("340000","3430200")
    check3 = tenkifunction.warnings("340000","3430700")
    check4 = tenkifunction.warnings("340000","3430400")
    check5 = tenkifunction.warnings("340000","3420700")
    check6 = tenkifunction.warnings("340000","3420200")
    check7 = tenkifunction.warnings("340000","3436800")
    check8 = tenkifunction.warnings("340000","3520800")
    check9 = tenkifunction.warnings("340000","3410100")
    check10 = tenkifunction.warnings("340000","3410200")
    check11 = tenkifunction.warnings("340000","3410300")
    check12 = tenkifunction.warnings("340000","3410400")
    check13 = tenkifunction.warnings("340000","3410500")
    check14 = tenkifunction.warnings("340000","3410600")
    check15 = tenkifunction.warnings("340000","3410700")
    check16 = tenkifunction.warnings("340000","3410800")
    check17 = tenkifunction.warnings("340000","3420300")
    check18 = tenkifunction.warnings("340000","3420500")
    check19 = tenkifunction.warnings("340000","3420800")
    check20 = tenkifunction.warnings("340000","3420900")
    check21 = tenkifunction.warnings("340000","3421000")
    check22 = tenkifunction.warnings("340000","3421100")
    check23 = tenkifunction.warnings("340000","3421300")
    check24 = tenkifunction.warnings("340000","3421400")
    check25 = tenkifunction.warnings("340000","3421500")
    check26 = tenkifunction.warnings("340000","3430900")
    check27 = tenkifunction.warnings("340000","3436800")
    check28 = tenkifunction.warnings("340000","3436800")
    check29 = tenkifunction.warnings("340000","3443100")
    check30 = tenkifunction.warnings("340000","3446200")
    check31 = tenkifunction.warnings("340000","3454500")
    check32 = tenkifunction.warnings("340000","3420400")
    if "注意報" in check and "警報" in check and "ありません" in check :
        return (check)
