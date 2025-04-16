# from sklearn.feature_extraction.text import TfidfVectorizer  
# from sklearn.cluster import KMeans  

# # Simple document collection with 3 documents
# docs = [
#     "Cats are agile and graceful animals",  
#     "Dogs are loyal companions to humans",  
#     "Sun rises in east and sets in west"
# ]  

# # Create TF-IDF vectors and cluster in fewer steps
# tfidf = TfidfVectorizer(stop_words='english').fit_transform(docs)
# labels = KMeans(n_clusters=3, random_state=0).fit_predict(tfidf)

# print("Cluster labels:", labels)


#!SLIPPP
# from sklearn.feature_extraction.text import TfidfVectorizer  
# from sklearn.cluster import KMeans
# import numpy as np

# # Document collection
# docs = [
#     "Machine learning is the study of computer algorithms that improve through experience.",
#     "Deep learning is a subset of machine learning.",
#     "Natural language processing is a field of artificial intelligence.",
#     "Computer vision is a field of study that enables computers to interpret the visual world.",
#     "Reinforcement learning is a machine learning algorithm.",
#     "Information retrieval is the process of obtaining information from a collection.",
#     "Text mining is the process of deriving high-quality information from text.",
#     "Data clustering is the task of dividing a set of objects into groups.",
#     "Hierarchical clustering builds a tree of clusters.",
#     "K-means clustering is a method of vector quantization."
# ]

# # Convert documents to TF-IDF vectors
# vectorizer = TfidfVectorizer(stop_words='english')
# X = vectorizer.fit_transform(docs)

# # Apply K-means clustering (k=3)
# k = 3
# kmeans = KMeans(n_clusters=k, random_state=42)
# clusters = kmeans.fit_predict(X)

# # Display results
# print(f"Documents grouped into {k} clusters:")
# for i in range(k):
#     print(f"\nCluster {i+1}:")
#     for j, doc in enumerate(docs):
#         if clusters[j] == i:
#             print(f"- {doc}")



#!!Newgroup
# # Simple K-means clustering on 20 Newsgroups dataset
# from sklearn.datasets import fetch_20newsgroups
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans

# # Load a small subset of the dataset (3 categories only)
# categories = ['comp.graphics', 'sci.med', 'rec.sport.baseball']
# data = fetch_20newsgroups(categories=categories, subset='train',)

# # Convert text to vectors and cluster
# vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
# vectors = vectorizer.fit_transform(data.data)
# kmeans = KMeans(n_clusters=3, random_state=42).fit(vectors)

# # Print results
# for i in range(3):
#     # Find documents in this cluster
#     docs_in_cluster = [idx for idx, label in enumerate(kmeans.labels_) if label == i]
#     count = len(docs_in_cluster)
    
#     # Get a sample document from this cluster
#     if docs_in_cluster:
#         sample_idx = docs_in_cluster[0]
#         sample_text = data.data[sample_idx][:50] + "..."
#         sample_category = data.target_names[data.target[sample_idx]]
        
#         print(f"Cluster {i+1}: {count} documents")
#         print(f"Sample ({sample_category}): {sample_text}")
#         print()

#?Newgroup
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load 20 Newsgroups dataset with selected categories
newsgroups = fetch_20newsgroups(subset='all', categories=[
    'alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med'
])

# Create TF-IDF vectors
tfidf = TfidfVectorizer(stop_words='english').fit_transform(newsgroups.data)

# Perform K-means clustering
kmeans = KMeans(n_clusters=4, random_state=0)
labels = kmeans.fit_predict(tfidf)

# Output cluster labels
print("Cluster labels:", labels)