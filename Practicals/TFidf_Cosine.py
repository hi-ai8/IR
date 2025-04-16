from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Corpus and query
documents = [
    "Document about python programming language and data analysis.",
    "Document discussing machine learning algorithms and programming techniques.",
    "Overview of natural language processing and its applications."
]
query = ["python programming"]

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform(query)

# Display TF-IDF vectors
print("TF-IDF Matrix for Documents:")
print(doc_vectors.toarray())

print("\nTF-IDF Vector for Query:")
print(query_vector.toarray())

# Calculate cosine similarity between query and each document
cosine_similarities = cosine_similarity(query_vector, doc_vectors).flatten()

# Print results
print("\nCosine Similarities between query and each document:")
for idx, score in enumerate(cosine_similarities, 1):
    print(f"Document {idx}: {score:.4f}")
