KNOWN ISSUES

Must be listening to music when the queue is being made

Will timeout sometimes



SETUP:

Run the commands 

$env:SPOTIPY_CLIENT_SECRET = 'bc1a1e0ca87d45d0b8cd0b4faca09217' 

$env:SPOTIPY_CLIENT_ID = 'cfc38a177d8c44d6ab871b93b0f4f072' 

$env:SPOTIPY_REDIRECT_URI = 'https://google.us/'

python ./actual-shuffle.py "Your spotify username goes here"

this will launch a web browser to authorize the application. press yes and copy+paste the url afterwards into the command line

the script should start indexing.
