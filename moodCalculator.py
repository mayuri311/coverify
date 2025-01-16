import statistics

class moodCalculator:
    def __init__(self):
        return

    def metricMeans(self, tracks):
        metrics = {"happiness": [], "colorContrast": [], "abstractness": [], "positivity": []}
        for track in tracks:
            print(track)
            metrics["happiness"].append(track["metadata"]["danceability"])
            metrics["colorContrast"].append(track["metadata"]["loudness"])
            metrics["abstractness"].append(track["metadata"]["energy"])
            metrics["positivity"].append(track["metadata"]["valence"])
        metrics["meanHappiness"] = statistics.mean(metrics["happiness"])
        metrics["meanColorContrast"] = statistics.mean(metrics["colorContrast"])
        metrics["meanAbstractness"] = statistics.mean(metrics["abstractness"])
        metrics["meanPositivity"] = statistics.mean(metrics["positivity"])
        return metrics

    def findTopSongs(self, tracks):
        sortedSongs = (sorted(tracks, key=lambda x: x["popularity"], reverse=True))
        topThreeSongs = [sortedSongs[0]["name"], sortedSongs[1]["name"], sortedSongs[2]["name"]]
        return topThreeSongs

    def analyzeHappiness(self, metrics):
        if metrics["meanHappiness"] > 0.5:
            return "happy sentiment"
        else:
            return "sad sentiment"

    def analyzeColorContrast(self, metrics):
        if metrics["meanColorContrast"] < -30:
            return "high color contrast"
        elif metrics["meanColorContrast"] >= -30:
            return "low color contrast"

    def analyzeAbstractness(self, metrics):
        if metrics["meanAbstractness"] > 0.5:
            return "intense."
        else:
            return "abstract and calm."

    def analyzePositivity(self, metrics):
        if metrics["meanPositivity"] > 0.5:
            return "happy, cheerful, and euphoric."
        else:
            return "sad, depressed, and angry."
