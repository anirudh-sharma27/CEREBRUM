from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

analyzer = SentimentIntensityAnalyzer()

# Load memory
with open("memory.json", "r") as f:
    memory = json.load(f)

trends = []

for entry in memory:
    reflection = entry["reflection"]
    embedding = entry["embedding"] 
    fog_score = entry.get("fog_before", None)
    date = entry.get("timestamp", None)  
    sentiment_score = analyzer.polarity_scores(reflection)
    compound = sentiment_score["compound"]

    if compound >= 0.05:
        sentiment = "positive"
    elif compound <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    trends.append({
        "reflection": reflection,
        "sentiment": sentiment,
        "compound_score": compound,
        "fog_score": fog_score,
        "date": date
    })

# Save to trends.json
with open("trends.json", "w") as f:
    json.dump(trends, f, indent=2)
