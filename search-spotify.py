import sys
import spotifyapi

spotify = spotifyapi.Session()

print(spotify.search(" ".join(sys.argv[1:]))["tracks"]["items"][0]["external_urls"]["spotify"])
