"""
Vector space model with TF-IDF and cosine similarity
"""
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Document corpus
docs = [
    "Document about python programming language and data analysis.",
    "Document discussing machine learning algorithms and programming techniques.",
    "Overview of natural language processing and its applications."
]

# Query
query = "python programming"

# Create TF-IDF vectors for documents and query
tfidf = TfidfVectorizer(stop_words='english')
# Fit on documents and query together to ensure shared vocabulary
all_texts = docs + [query]
tfidf.fit(all_texts)

# Transform documents and query to TF-IDF vectors
docs_tfidf = tfidf.transform(docs).toarray()
query_tfidf = tfidf.transform([query]).toarray()[0]

# Calculate cosine similarity
def cosine_sim(v1, v2):
    dot = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    return dot / (norm1 * norm2) if norm1*norm2 != 0 else 0

# Calculate and display similarity between query and each document
print(f"Query: '{query}'")
print("\nCosine Similarity Results:")
for i, doc in enumerate(docs):
    similarity = cosine_sim(query_tfidf, docs_tfidf[i])
    print(f"Document {i+1}: {similarity:.4f}")
    print(f"  Text: {doc}")
    
#! Part B: Cosine similarity for specific query and document
query_B = "gold silver truck"
doc_B = "shipment of gold damaged in a gold fire"

# Create new vectorizer for Part B
tfidf_B = TfidfVectorizer(stop_words='english')
tfidf_B.fit([query_B, doc_B])  # Fit both to get shared vocabulary

# Transform query and document
query_vector_B = tfidf_B.transform([query_B]).toarray()[0]
doc_vector_B = tfidf_B.transform([doc_B]).toarray()[0]

# Calculate similarity
similarity_B = cosine_sim(query_vector_B, doc_vector_B)

# Print Part B results
print("\nPart B: Cosine Similarity")
print(f"Query: '{query_B}'")
print(f"Document: '{doc_B}'")
print(f"Similarity: {similarity_B:.4f}")
