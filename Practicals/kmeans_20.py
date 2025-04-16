from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load the 20 Newsgroups dataset (just a subset for simplicity)
newsgroups = fetch_20newsgroups(subset='all')  # 'all' will load both training and test sets

# Vectorize the documents using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)  # Limit features for simplicity
X = vectorizer.fit_transform(newsgroups.data)

# Apply K-means clustering with 5 clusters (you can adjust the number of clusters)
kmeans = KMeans(n_clusters=5, random_state=0).fit(X)

# Output the labels (cluster assignments)
print(kmeans.labels_)
