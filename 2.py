import gensim.downloader as api
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

model = api.load("word2vec-google-news-300")

tech_words = [
    "computer", "internet", "software", "hardware", 
    "network", "database", "data", "server", 
    "programming", "algorithm"
]

vectors = [model[word] for word in tech_words]

pca = PCA(n_components=2)
vectors_2d = pca.fit_transform(vectors)

plt.figure(figsize=(10, 6))
for i, word in enumerate(tech_words):
    x, y = vectors_2d[i]
    plt.scatter(x, y, marker='o', color='blue')
    plt.text(x + 0.02, y + 0.02, word, fontsize=12)

plt.title("2D PCA Projection of Technology-related Word Embeddings")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid(True)
plt.show()

def generate_similar_words(input_word, topn=5):
    try:
        similar_words = model.most_similar(positive=[input_word], topn=topn)
        print(f"Top {topn} words similar to '{input_word}':")
        for word, similarity in similar_words:
            print(f"{word} : similarity = {similarity:.6f}")
    except KeyError:
        print(f"The word '{input_word}' is not in the vocabulary.")

user_input = input("Enter a word (e.g., 'internet'): ")
generate_similar_words(user_input)
