import re
import spotifyapi
import tidalapi

def get_id (url: str) -> str:
    """Get the ID of the item from a Tidal link."""
    matches = re.search(r"https://tidal.com/browse/.*/([0-9]*)", url)
    if matches:
        return matches.groups()[0]
    return ""

def get_url (url: str, spotify: spotifyapi.Session, tidal: tidalapi.Session) -> str | None:
    tidal_track_id = get_id(url)
    track = tidal.track(tidal_track_id)

    t = url.split("/")[4]
    ts = t + "s"
    search = "{} {}".format(track.name, track.artist.name)
    result = spotify.search(search, [ t ], 1)[ts]["items"][0]

    return result["external_urls"]["spotify"]
