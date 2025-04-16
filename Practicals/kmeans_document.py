from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

documents = [
    "Cats are known for their agility and grace",  # cat doc1
    "Dogs are often called 'man's best friend.",  # dog doc1
    "Some dogs are trained to assist people with disabilities.",  # dog doc2
    "The sun rises in the east and sets in the west.",  # sun doc1
    "Many cats enjoy climbing trees and chasing toys."  # cat doc2
]

# Convert documents into TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# Print the cluster labels for each document
print(kmeans.labels_)
