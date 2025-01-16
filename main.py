import imageGenerator
import musicService
import moodCalculator
import configuration
import argparse
import sys

parser = argparse.ArgumentParser(description="Spotify playlist cover generator")
parser.add_argument("--configfile", nargs='?', default="spotify.ini")
args = parser.parse_args()

# configuring spotify api
config = configuration.configuration(args.configfile)
spotifyConfiguration = config.readSection("spotify")
spotify = musicService.musicService(spotifyConfiguration)

# extracting user info
spotify.authenticate()
playlists = spotify.userPlaylists('b85732r3t2grqvvh9vf4vux0u')
tracks = spotify.extractTracks('4LIk4ZC6DCV3tx9c6PKvGs')

# extracting playlist info
calculator = moodCalculator.moodCalculator()
metrics = calculator.metricMeans(tracks)
topSongs = calculator.findTopSongs(tracks)

# audio feature analysis

happiness = calculator.analyzeHappiness(metrics)
abstractness = calculator.analyzeAbstractness(metrics)
positivity = calculator.analyzePositivity(metrics)
colorContrast = calculator.analyzeColorContrast(metrics)

# image generation

ig = imageGenerator.imageGenerator()
prompt = ig.promptBuilder(happiness, abstractness, colorContrast, positivity, topSongs)
print(prompt)
imageURL = ig.generation(prompt)
print(imageURL)
