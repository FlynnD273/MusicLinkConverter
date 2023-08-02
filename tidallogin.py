from plyer import notification
import datetime
import os
import tidalapi
import pickle

def login () -> tidalapi.Session:
    def login (session: tidalapi.Session) -> None:
        login, future = session.login_oauth()
        notification.notify("Open the URL to log in", login.verification_uri_complete)
        future.result()

    tidal_session = tidalapi.Session()
    picklepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tidalsession.pickle")
    if os.path.exists(picklepath):
        with open(picklepath, "rb") as f:
            store = pickle.load(f)
        if store["time"] > datetime.datetime.now() + datetime.timedelta(minutes= 10):
            tidal_session.load_oauth_session(store["type"], store["token"], expiry_time= store["time"])
        else:
            login(tidal_session)
    else:
        login(tidal_session)

    if not tidal_session.check_login():
        print("Failed to log in. Please try again later.")
        os.remove(picklepath)
        exit(1)

    store = { 
             "type": tidal_session.token_type,
             "token": tidal_session.access_token,
             "time": tidal_session.expiry_time,
             }
    with open(picklepath, "wb") as f:
        pickle.dump(store, f)
    
    return tidal_session

