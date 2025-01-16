from fastapi import FastAPI
import uvicorn
from fastapi import Request
from pydantic import BaseModel
from fastapi import Response, status
import imageGenerator
import musicService
import moodCalculator
import configuration
import argparse
from datetime import datetime


# rest api documentation shows up in
#
#    http://127.0.0.1:8000/docs

parser = argparse.ArgumentParser(description="Spotify playlist cover generator")
parser.add_argument("--configfile", nargs='?', default="spotify.ini")
args = parser.parse_args()

app = FastAPI()

# configuring spotify api
config = configuration.configuration(args.configfile)
spotifyConfiguration = config.readSection("spotify")
app.spotify = musicService.musicService(spotifyConfiguration)

# extracting user info
app.spotify.authenticate()

app.userID_cache = ''
app.playlistID_cache = ''


@app.get("/coverify/setUserID/{userID}")
async def setUserID(userID: str):
    print(userID)
    app.userID_cache = userID
    return status.HTTP_200_OK


@app.get("/coverify/getPlaylists/")
async def getPlaylists():
    playlists = app.spotify.userPlaylists(app.userID_cache)
    return playlists



@app.get("/coverify/setPlaylist/{playlist}")
async def setPlaylist(playlistID: str):
    app.playlistID_cache = playlistID
    return status.HTTP_200_OK


@app.get("/coverify/getImageURL/")
async def getImageURL():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    tracks = app.spotify.extractTracks(app.playlistID_cache)
    calculator = moodCalculator.moodCalculator()
    metrics = calculator.metricMeans(tracks)
    topSongs = calculator.findTopSongs(tracks)
    happiness = calculator.analyzeHappiness(metrics)
    abstractness = calculator.analyzeAbstractness(metrics)
    positivity = calculator.analyzePositivity(metrics)
    colorContrast = calculator.analyzeColorContrast(metrics)
    ig = imageGenerator.imageGenerator()
    prompt = ig.promptBuilder(happiness, abstractness, colorContrast, positivity, topSongs)
    imageURL = ig.generation(prompt)
    print(prompt)
    print(imageURL)
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    return {"image url": imageURL}


if __name__ == "__main__":
    uvicorn.run("coverifyBackend:app", host="0.0.0.0", port=8000, reload=True)
