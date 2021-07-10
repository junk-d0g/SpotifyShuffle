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
scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-read-private playlist-read-collaborative user-library-read'

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

playlists = spotifyObject.current_user_playlists()
playlists.update(spotifyObject.user_playlists(username))

#index the users playlist
user_lists = {"My Liked Songs":0}
while playlists:
    for i, playlist in enumerate(playlists['items']):
        user_lists.update({playlist['name']:playlist['uri']})
    if playlists['next']:
        playlists = spotifyObject.next(playlists)
    else:
        playlists = None

#User chooses target playlist
for playlist in user_lists:
    print(playlist)
target = input("What do you want to play? title, case sensitive: ")
while target not in user_lists:
    print("That wasn't an option")
    target = input("Spell it right this time: ")
target = user_lists.get(target)
song_num = (int)(input("How many songs do you want to queue (Spotify really doesn't like large queues): "))

print("Indexing")

#if the user chose an actual playlist, spotify allows reading in the playlist as an object
#if the user would like to choose from their liked songs, index it to get the length and create a list of songs
if target != 0:
    hog = spotifyObject.playlist(target)['tracks']['items']

    for track in hog:
        uri = track['track']['uri']
        songs.append(uri)
else:
    while True:
        print("adding index ",end='')
        print(off)
        try:
            hog = spotifyObject.current_user_saved_tracks(limit=amount, offset=off)['items']
            if len(hog) == 0:
                break
            for track in hog:
                uri = track['track']['uri']
                songs.append(uri)

            off+=amount
        except Exception:
            break
#once the list of songs is created, add to queue
for i in range(song_num):
        rand = random.randint(0,len(songs)-1)
        spotifyObject.add_to_queue(songs[rand])
        print("Added song number",i+1)
