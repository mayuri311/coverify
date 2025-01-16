import requests


class musicService:
    def __init__(self, spotifyConfiguration):
        self.CLIENT_ID = spotifyConfiguration["CLIENT_ID"]
        self.CLIENT_SECRET = spotifyConfiguration["CLIENT_SECRET"]
        self.AUTH_URL = spotifyConfiguration["AUTH_URL"]
        self.BASE_URL = spotifyConfiguration["BASE_URL"]

    def authenticate(self):
        auth_response = requests.post(self.AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
        })
        auth_response_data = auth_response.json()
        # save the access token
        self.access_token = auth_response_data['access_token']
        self.headers = {'Authorization': 'Bearer {token}'.format(token=self.access_token)}

    def userPlaylists(self, userID):
        playlists = []
        r = requests.get(self.BASE_URL + 'users/' + userID + '/playlists', headers=self.headers)
        userPlaylistData = r.json()
        items = userPlaylistData["items"]
        for item in items:
            playlist = {"name": item["name"], "id": item["id"]}
            playlists.append(playlist)
        return playlists

    def getUserPfp(self, userID):
        r = requests.get(self.BASE_URL + 'users/' + userID, headers=self.headers)
        userData = r.json()
        image_href = userData["images"]["url"]
        return image_href

    def extractSongData(self, songID):
        r = requests.get(self.BASE_URL + 'audio-features/' + songID, headers=self.headers)
        trackData = r.json()
        return trackData

    def extractTracks(self, playlistID):
        tracks = []
        r = requests.get(self.BASE_URL + 'playlists/' + playlistID + '/tracks', headers=self.headers)
        trackData = r.json()
        items = trackData["items"]
        for item in items:
            track = {"name": item["track"]["name"], "id": item["track"]["id"], "artist": item["track"]["artists"][0]["name"], "album": item["track"]["name"], "popularity": item["track"]["popularity"]}
            track["metadata"] = self.extractSongData(track["id"])
            tracks.append(track)
        return tracks



















