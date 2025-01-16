import requests

CLIENT_ID = 'c9fce2ac32fc4962bf22a001a0153c12'
CLIENT_SECRET = 'fa16c95ceb554cac902d7c84d0b62985'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

# header
headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
user_id = 'b85732r3t2grqvvh9vf4vux0u'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

# convert response to json
r = r.json()

class MusicService:
    def authorizeCredentials:

    def askForPlaylist:


class MoodCalculator:
    def analyzePlaylistMetrics:

    def analyzeSongMetrics

class PromptGeneration:

    def phrase:



print(r)