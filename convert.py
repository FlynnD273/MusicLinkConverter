from plyer import notification
import datetime
import sys
import os
import spotifyapi
import tidalapi
import pickle
import spotify2tidal
import tidal2spotify

spotify_session = spotifyapi.Session()

def login (session: tidalapi.Session) -> None:
    login, future = session.login_oauth()
    notification.notify("Open the URL to log in", login.verification_uri_complete)
    future.result()

tidal_session = tidalapi.Session()
if os.path.exists("tidalsession.pickle"):
    with open("tidalsession.pickle", "rb") as f:
        store = pickle.load(f)
    if store["time"] > datetime.datetime.now() + datetime.timedelta(minutes= 10):
        tidal_session.load_oauth_session(store["type"], store["token"], expiry_time= store["time"])
    else:
        login(tidal_session)
else:
    login(tidal_session)

if not tidal_session.check_login():
    print("Failed to log in. Please try again later.")
    os.remove("tidalsession.pickle")
    exit(1)

store = { 
         "type": tidal_session.token_type,
         "token": tidal_session.access_token,
         "time": tidal_session.expiry_time,
         }
with open("tidalsession.pickle", "wb") as f:
    pickle.dump(store, f)

if len(sys.argv) > 1:
    url = sys.argv[1]
    if url.startswith("https://open.spotify.com/"):
        print(spotify2tidal.get_url(url, spotify_session, tidal_session))
    elif url.startswith("https://tidal.com/browse/"):
        print(tidal2spotify.get_url(url, spotify_session, tidal_session))
