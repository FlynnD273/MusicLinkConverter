from getpass import getpass
import re
import requests

def get_id (url: str) -> str:
    """Get the ID of the item from a Tidal link."""
    matches = re.search(r"https://tidal.com/browse/.*/([0-9]*)", url)
    if matches:
        return matches.groups()[0]
    return ""

def get_access_token () -> str:
    """Get a Tidal access token"""
    params= { "token": "kgsOOmYk3zShYrNP" }
    username = input("Enter you Tidal email address: ")
    password = getpass("Enter your password: ")
    data = { "username": username, "password": password }
    r = requests.post("https://api.tidal.com/v1/login/username", params= params, data= data)
    print(r.request.path_url)
    print(r)
    print(r.text)
    return "kgsOOmYk3zShYrNP"

def api (access_token: str, query: str, params: dict[str, str] | None = None):
    """Call the Tidal API. Returns the parsed JSON object."""
    header = { "x-tidal-token": access_token }
    r = requests.get("https://api.tidal.com/v1"+query, params= params, headers= header)
    print(r)
    print(r.text)
    print(r.json)
    return ""
    # return json.loads(r.text, object_hook=lambda d: SimpleNamespace(**d))

