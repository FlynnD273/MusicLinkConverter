import spotifyapi
import tidalapi

def get_url (url: str, spotify: spotifyapi.Session, tidal: tidalapi.Session) -> str | None:
    spotify_track_id = spotifyapi.get_id(url)

    t = url.split("/")[3]
    ts = t + "s"
    track = spotify.query("/{}/{}".format(ts, spotify_track_id))
    search = "{} {}".format(track["name"], track["artists"][0]["name"])
    result = tidal.search(search, models= [tidalapi.Track, tidalapi.Album, tidalapi.Artist], limit= 1)[ts][0]

    return "https://listen.tidal.com/{}/{}".format(t, str(result.id))
