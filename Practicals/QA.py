from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "The cat is on the mat.",
    "The dog is in the yard.",
    "A bird is flying in the sky.",
    "The sun is shining brightly."
]

query = "Where is the cat?"

# Vectorize documents and query
vectorizer = TfidfVectorizer().fit(documents + [query])
doc_vecs = vectorizer.transform(documents)
query_vec = vectorizer.transform([query])

# Find most similar document
best_match = cosine_similarity(query_vec, doc_vecs).argmax()
print("Answer:", documents[best_match])
