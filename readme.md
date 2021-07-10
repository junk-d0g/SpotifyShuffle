KNOWN ISSUES

Must be listening to music when the queue is being made

Will timeout sometimes



SETUP:

python ./actual-shuffle.py "Your spotify username goes here"

this will launch a web browser to authorize the application. press yes and copy+paste the url afterwards into the command line

the script should start indexing.


TO DO

Test with a playlist larger than 50 songs, make sure that spotify allows that pull

    If spotify allows that, consider creating a hidden playlist so we can pull the whole thing at once

If the playlist method doesn't work, consider threading

Allow mixing of playlists

Integrate a search