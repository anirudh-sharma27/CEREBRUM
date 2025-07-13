
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The Sandman is a great show",
    "I Love KFC",
    "The Sandman and Death and Desire are siblings",
    "I love the 2nd season of The Sandman",
    "I love to eat the zinger from KFC",
    "My cat is a bitch",
    "I have a dog named Morpheous inspired from my favorite show",
    "My Cat's name is Oneiros"
]
embeddings = model.encode(sentences)

#Compute cosine similarity between all pairs
cos_sim = util.cos_sim(embeddings, embeddings)

print(cos_sim)
#most similar sentences
#Add all pairs to a list with their cosine similarity score
all_sentence_combinations = []
for i in range(len(cos_sim)-1):
    for j in range(i+1, len(cos_sim)):
        all_sentence_combinations.append((cos_sim[i][j], i, j))
all_sentence_combinations   


#Sort list by the highest cosine similarity score
all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[0], reverse=True)

print("Top-5 most similar pairs:")
for score, i, j in all_sentence_combinations[0:5]:
    print("{} \t {} \t {:.4f}".format(sentences[i], sentences[j], cos_sim[i][j]))