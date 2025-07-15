import json
import openai

with open("trends.json", "r") as f:
    data = json.load(f)

reflections = [entry["reflection"] for entry in data]
sentiment = [entry["sentiment"] for entry in data]
fog_score = [entry["fog_score"] for entry in data]
compound_score = [entry["coumpound_score"] for entry in data]
date = [entry["date"] for entry in data]

