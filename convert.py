import sys
import spotifyapi
import tidallogin
import spotify2tidal
import tidal2spotify

spotify_session = spotifyapi.Session()

tidal_session = tidallogin.login()

if len(sys.argv) > 1:
    url = sys.argv[1]
    if url.startswith("https://open.spotify.com/"):
        print(spotify2tidal.get_url(url, spotify_session, tidal_session))
    elif url.startswith("https://tidal.com/browse/"):
        print(tidal2spotify.get_url(url, spotify_session, tidal_session))
    elif url.startswith("https://listen.tidal.com"):
        url = url.replace("https://listen.tidal.com", "https://tidal.com/browse")
        print(tidal2spotify.get_url(url, spotify_session, tidal_session))
