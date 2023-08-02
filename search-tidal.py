import sys
import tidallogin
import tidalapi

tidal = tidallogin.login()

result = tidal.search(sys.argv[1], models= [ tidalapi.Track ], limit= 1)["tracks"][0]

print("https://listen.tidal.com/track/" + str(result.id))
