import spotipy
import json
import random
import os
import sys
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from json.decoder import JSONDecodeError

username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state user-library-read'

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)

tracks = spotifyObject.current_user_saved_tracks()['items']
songs = []

run = True
off = 0
print("starting indexing")
while run:
    print("adding index ",end='')
    print(off)
    try:
        spotifyObject.current_user_saved_tracks(limit=1,offset=off)
        uri = spotifyObject.current_user_saved_tracks(limit=1, offset=off)['items'][0]['track']['uri']
        songs.append(uri)
        off+=1
    except Exception:
        run = False
        break

print("finished indexing")
print("adding random indexes to queue")
for i in range(len(songs)):
    rand = random.randint(0,len(songs)-1)
    spotifyObject.add_to_queue(songs[rand])
    songs.remove(songs[rand])

#['items'][0]['track']['track_number']