import io
import os
from notifypy import Notify
import sys
import requests
import bs4
from PIL import Image
from datetime import datetime
import tidalapi

import tidallogin

iconpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{hash(datetime.now())}.png")
tidal = tidallogin.login()

search = tidal.search(sys.argv[1], models= [ tidalapi.Track ], limit= 1)["tracks"]
track = search[0]
desc = f"{track.full_name} - {', '.join([a.name for a in track.artists])}"

imgurl = track.album.image(320)
imgreq = requests.get(imgurl)

img = Image.open(io.BytesIO(imgreq.content))
img.save(iconpath)

notif = Notify()

notif.title = "Search Result"
notif.message = desc
notif.icon = iconpath

notif.send()

print("https://listen.tidal.com/track/" + str(track.id))

os.remove(iconpath)
