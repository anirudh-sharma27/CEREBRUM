import numpy as np
from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("memory.json","r") as f:
    data = json.load(f)

reflections = [entry["reflection"] for entry in data]
embeddings = [entry["embedding"] for entry in data]

query = input("what would you like to search for?")
query_vec = model.encode(query)

#cosine similarity
def cosine_sim(a,b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b))


scores = [cosine_sim(query_vec,emb) for emb in embeddings]

top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]

print("Top 3 reflections:")
for idx in top_indices:
    entry = data[idx]
    print(f"Timestamp: {entry['timestamp']}, Fog Before: {entry['fog_before']}, Fog After: {entry['fog_after']}")
    print(f"Reflection: {entry['reflection']}")         


    






