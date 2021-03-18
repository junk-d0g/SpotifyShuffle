import spotipy
import json
import random
import os
import time
import sys
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from json.decoder import JSONDecodeError
import json

random.seed(time.time())
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state user-library-read'

os.environ["SPOTIPY_CLIENT_SECRET"] = "bc1a1e0ca87d45d0b8cd0b4faca09217"
os.environ["SPOTIPY_CLIENT_ID"] = "cfc38a177d8c44d6ab871b93b0f4f072"
os.environ["SPOTIPY_REDIRECT_URI"] = "https://google.us/"

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)

tracks = spotifyObject.current_user_saved_tracks()['items']
songs = []

amount = 50

off = 0
print("starting indexing")
while True:
    print("adding index ",end='')
    print(off)
    try:
        hog = spotifyObject.current_user_saved_tracks(limit=amount, offset=off)['items']
        if len(hog) == 0:
            break
        for track in hog:
            #print(json.dumps(track, indent=4))
            #print("#############################################################")
            uri = track['track']['uri']
            #print(uri)
            #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            songs.append(uri)
        off+=amount
    except Exception:
        break
inp = 0
print("finished indexing")
inp = int(input("How many songs would you like to add?\nSpotify Desktop does not handle queues over 1000 very well\n"))

for i in range(inp):
    rand = random.randint(0,len(songs)-1)
    spotifyObject.add_to_queue(songs[rand])
    print(str(inp-i)+" songs remaining")
print("Finished!")

#['items'][0]['track']['track_number']