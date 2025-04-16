# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# from collections import Counter

# # Download resources once
# try:
#     nltk.data.find('tokenizers/punkt')
#     nltk.data.find('corpora/stopwords')
# except LookupError:
#     nltk.download('punkt', quiet=True)
#     nltk.download('stopwords', quiet=True)

# def extractive_summary(text, num_sentences=3):
#     # Tokenize and filter stopwords
#     stop_words = set(stopwords.words('english'))
#     words = [word.lower() for word in word_tokenize(text) 
#              if word.lower() not in stop_words and word.isalnum()]
    
#     # Calculate normalized word frequencies
#     word_freq = Counter(words)
#     max_freq = max(word_freq.values()) if word_freq else 1
#     word_freq = {word: count/max_freq for word, count in word_freq.items()}
    
#     # Score sentences based on word frequencies
#     sentences = sent_tokenize(text)
#     sentence_scores = {}
    
#     for sentence in sentences:
#         for word in word_tokenize(sentence.lower()):
#             if word in word_freq:
#                 sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]
    
#     # Get top N sentences and join them
#     summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
#     return ' '.join(summary_sentences)

# # Example usage
# if __name__ == "__main__":
#     text = """
#     Technology has dramatically transformed society in the past few decades. From the 
#     invention of the internet to the rise of artificial intelligence, technology has 
#     fundamentally altered how we communicate, work, and live our daily lives. The digital 
#     age has brought both immense opportunities and challenges, impacting everything 
#     from business practices to social structures. 
#     One of the most significant ways in which technology has aAected society is through 
#     the rapid expansion of communication channels. The advent of the internet, social 
#     media platforms, and smartphones has made it easier for people to connect globally, 
#     breaking down geographical barriers. Social media platforms like Facebook, Twitter, and 
#     Instagram allow people to share ideas, opinions, and news instantaneously. The ability 
#     to communicate with people from all corners of the world has fostered a sense of 
#     interconnectedness that was previously unimaginable. 
#     In the business world, technology has revolutionized how companies operate. 
#     Automation and data analytics have made it possible for businesses to streamline 
#     processes, improve eAiciency, and make data-driven decisions. E-commerce has 
#     transformed retail, allowing businesses to reach global markets without the need for 
#     physical stores. Cloud computing and collaboration tools have enabled remote work, 
#     giving rise to flexible work arrangements and digital nomadism.
#     """
    
#     print(extractive_summary(text))



#!small
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# from collections import Counter

# # Download required NLTK resources
# nltk.download('punkt', quiet=True)
# nltk.download('stopwords', quiet=True)

# def summarize(text, num_sentences=3):
#     # Tokenize text into sentences and words
#     sentences = sent_tokenize(text)
#     stop_words = set(stopwords.words('english'))
    
#     # Count word frequencies (excluding stopwords)
#     words = [word.lower() for word in word_tokenize(text) 
#              if word.lower() not in stop_words and word.isalnum()]
#     word_freq = Counter(words)
    
#     # Score sentences based on word frequency
#     scores = {}
#     for sentence in sentences:
#         for word in word_tokenize(sentence.lower()):
#             if word in word_freq:
#                 scores[sentence] = scores.get(sentence, 0) + word_freq[word]
    
#     # Get top sentences
#     summary = sorted(scores, key=scores.get, reverse=True)[:num_sentences]
#     return ' '.join(summary)

# # Example
# if __name__ == "__main__":
#     text = """
#     Artificial intelligence is transforming industries worldwide. Machine learning 
#     algorithms can analyze vast amounts of data to identify patterns. Natural language 
#     processing allows computers to understand human language. Computer vision enables 
#     machines to interpret and make decisions based on visual data. These technologies 
#     are creating new opportunities and challenges for businesses and society.
#     """
    
#     print(summarize(text))




# #?SMallest
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
text = """Artificial intelligence is transforming industries worldwide. Machine learning 
    algorithms can analyze vast amounts of data to identify patterns. Natural language 
    processing allows computers to understand human language. Computer vision enables 
    machines to interpret and make decisions based on visual data. These technologies 
    are creating new opportunities and challenges for businesses and society""" 
summary = extractive_summary(text, num_sentences=2) 
print("Summary:", summary) 
