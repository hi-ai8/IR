from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def extractive_summary(text, num_sentences=2):
    sentences = text.split('.')
    tfidf = TfidfVectorizer(stop_words='english').fit_transform(sentences)
    sim_matrix = cosine_similarity(tfidf)
    sentence_scores = sim_matrix.sum(axis=1)
    return '. '.join(np.array(sentences)[sentence_scores.argsort()[-num_sentences:]])

# Example usage
text = "Artificial intelligence (AI) is intelligence demonstrated by machines. AI research has been divided into subfields."
summary = extractive_summary(text, num_sentences=2)
print("Summary:", summary)
