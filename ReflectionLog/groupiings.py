import json
from sklearn.cluster import KMeans
import numpy as np

# Load reflections and embeddings
with open("memory.json", "r") as f:
    data = json.load(f)

reflections = [entry["reflection"] for entry in data]
embeddings = [entry["embedding"] for entry in data]

k = 2
km = KMeans(n_clusters=k, random_state=42)
labels = km.fit_predict(embeddings)

# Group reflections by cluster
clusters = {i: [] for i in range(k)}
for i, label in enumerate(labels):
    clusters[label].append(reflections[i])

# Print reflections grouped by cluster
for cluster_id, texts in clusters.items():
    print(f"\n Cluster {cluster_id} ({len(texts)} reflections):")
    for text in texts[:5]:  # Show up to 5 examples per cluster
        print(f" - {text}")
