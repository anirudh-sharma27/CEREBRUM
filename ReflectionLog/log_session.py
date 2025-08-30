from sentence_transformers import SentenceTransformer
import json
from keybert import KeyBERT
from datetime import datetime
import os


model = SentenceTransformer("all-MiniLM-L6-v2")


mood = float(input("How are you feeling today?(7-Very positive  ; 1 - Very negative):"))
focus = float(input("Rate your focus today(5-Very focused ;1 - No focus):"))
confidence = float(input("rate your confidence today(5- very confident ,1 - Not confident at all):"))
reflection = input("Enter your reflection for the session: ")


embedding = model.encode(reflection).tolist()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
tags = []


model = KeyBERT()

x = model.extract_keywords(reflection,keyphrase_ngram_range=(1,3))
print("Here are some curated tags from your Journal-")
for i in x:
    (a,b) = x[i]
    print(a)
    k = input("Keep this?:")
    if k in ["yes","Yes"]:
        tags.append(a)
    
k = input("Any other tag you would like to add?:")
if k!="no":
    tags.append(k)


entry = {
    "timestamp":now,
    "mood": mood,
    "focus":focus,
    "confidence":confidence,
    "tags":tags,
    "reflection": reflection,
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




