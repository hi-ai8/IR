# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# class SimpleQA:
#     def __init__(self, qa_dict):
#         self.questions = list(qa_dict.keys())
#         self.answers = list(qa_dict.values())
        
#         # Create and fit the vectorizer
#         self.vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
#         self.vectorizer.fit(self.questions + self.answers)
#         self.question_vectors = self.vectorizer.transform(self.questions)
        
#     def answer(self, question):
#         # Find most similar question and return its answer
#         q_vector = self.vectorizer.transform([question])
#         similarities = cosine_similarity(q_vector, self.question_vectors)[0]
#         return self.answers[similarities.argmax()]

# if __name__ == "__main__":
#     # Knowledge base
#     qa_pairs = {
#         "What is the capital of France?": "Paris is the capital of France.",
#         "Who painted the Mona Lisa?": "Leonardo da Vinci painted the Mona Lisa.",
#         "When did World War II end?": "World War II ended in 1945."
#     }
    
#     # Create QA system and test
#     qa_system = SimpleQA(qa_pairs)
#     print(qa_system.answer("which war ended in 1945?"))



#!slip
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Simple corpus
documents = [
    "The cat is on the mat.",
    "The dog is in the yard.",
    "A bird is flying in the sky.",
    "The sun is shining brightly."
]

# Create TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

def answer_question(question):
    # Transform question to vector
    question_vector = vectorizer.transform([question])
    
    # Find most similar document
    similarities = cosine_similarity(question_vector, tfidf_matrix)[0]
    best_match_index = similarities.argmax()
    
    # Return the most relevant document
    return documents[best_match_index]

# Test the system
question = "Where is the cat?"
answer = answer_question(question)
print(f"Question: {question}")
print(f"Answer: {answer}")