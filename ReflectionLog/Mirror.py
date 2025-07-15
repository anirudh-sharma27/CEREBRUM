import json
from LLMPractice import mirror
with open("trends.json", "r") as f:
    data = json.load(f)

reflections = [entry["reflection"] for entry in data]
sentiment = [entry["sentiment"] for entry in data]
fog_score = [entry["fog_score"] for entry in data]
compound_score = [entry["compound_score"] for entry in data]
date = [entry["date"] for entry in data]


prompt = "Here are recent reflections and scores:\n\n"
for i in range(-7, 0):  # last 7 entries
    prompt += f"{i+8}. \"{reflections[i]}\"\n"
    prompt += f"   Sentiment: {sentiment[i]}, Compound: {compound_score[i]}, Fog Score: {fog_score[i]}\n\n"

prompt += "Based on these entries, give a brief but emotionally intelligent summary of the user's current cognitive and emotional state. Focus on clarity, emotional tone, patterns, and recovery signs. Avoid exaggeration. Be calm and compassionate."
print("cerebrum says-","\n")
print(mirror(prompt))

