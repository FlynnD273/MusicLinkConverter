import json
from bs4 import BeautifulSoup
import re
import requests

def get_id (url: str) -> str:
    """Get the ID of the item from a Spotify link."""
    matches = re.search(r"https://open.spotify.com/.*/([0-9A-Za-z]*)", url)
    if matches:
        return matches.groups()[0]
    return ""

class Session:
    def __init__(self) -> None:
        self._access_token = self.__get_access_token__()
    def __get_access_token__ (self) -> str:
        """Get a temporary Spotify access token. This token lasts for an hour."""
        r = requests.get("https://open.spotify.com/")
        parsed = BeautifulSoup(r.text, features="lxml")
        parsed_json = json.loads(parsed.find(attrs={ "id":"session" }).text)
        return parsed_json["accessToken"]

    def query (self, query: str, params: dict[str, str] | None = None):
        """Call the Spotify API. Returns the parsed JSON object."""
        header = { "Authorization": "Bearer "+self._access_token }
        r = requests.get("https://api.spotify.com/v1"+query, params= params, headers= header)
        return json.loads(r.text)

    def search (self, search: str, categories: list[str] = [ "track" ], limit: int = 1):
        """Search Spotify.
        Valid categories are: album, artist, playlist, track, show, episode, audiobook
        Search result categories are returned as properties in the plural form"""
        return self.query("/search", { "q": search, "type": ",".join(categories), "limit": str(limit) })

