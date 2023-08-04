import io
import os
from notifypy import Notify
import sys
import requests
import bs4
from PIL import Image
from datetime import datetime

import spotifyapi

iconpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{hash(datetime.now())}.png")
spotify = spotifyapi.Session()
track = spotify.search(sys.argv[1])["tracks"]["items"][0]

desc = track["name"] + " - " + ", ".join([s["name"] for s in track["artists"]])
trackurl = track["external_urls"]["spotify"]

page = requests.get(trackurl).text
parsed = bs4.BeautifulSoup(page, features="lxml")

img_element = parsed.find("img", attrs={ "alt":track["name"] })
if not img_element:
    img_element = parsed.find("img", attrs={ "alt":"" })

imgurl = ""
if isinstance(img_element, bs4.Tag):
    if "srcset" in img_element:
        imgurl = str(img_element["srcset"]).split(", ")[-1].split(" ")[0]
    else:
        imgurl = str(img_element["src"])

has_icon = False
if imgurl != "":
    has_icon = True
    imgreq = requests.get(imgurl)

    img = Image.open(io.BytesIO(imgreq.content))
    img.save(iconpath)

notif = Notify()

notif.title = "Search Result"
notif.message = desc
if has_icon:
    notif.icon = iconpath

notif.send()

print(trackurl)

os.remove(iconpath)
