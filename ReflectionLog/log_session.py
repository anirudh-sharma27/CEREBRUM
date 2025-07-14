from sentence_transformers import SentenceTransformer
import json
from datetime import datetime
import os


model = SentenceTransformer("all-MiniLM-L6-v2")

fog_before = float(input("Enter your brainfog score before session(1-10)"))
reflection = input("Enter your reflection for the session: ")
fog_after = float(input("Enter your brainfog score after session(1-10)")) 


embedding = model.encode(reflection).tolist()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

entry = {
    "timestamp":now,
    "fog_before": fog_before,
    "reflection": reflection,
    "fog_after": fog_after,
    "embedding": embedding
}

file = "memory.json"

if os.path.exists(file):
    with open(file, "r") as f:
        data = json.load(f)
else:
    data = []

data.append(entry)

with open(file, "w") as f:
    json.dump(data, f, indent=4)
print("Entry saved")




