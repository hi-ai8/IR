import string

documents = {
    "Document 1": "BSc lectures start at 7.",
    "Document 2": "My lectures are over.",
    "Document 3": "Today is a holiday."
}
# Preprocess: lowercase and remove punctuation
def preprocess(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation)).split()

# Build inverted index
inverted_index = {}
occurrences = {}

for doc_id, text in documents.items():
    words = preprocess(text)
    occurrences[doc_id] = {}
    
    for term in set(words):
        if term not in inverted_index:
            inverted_index[term] = []
        inverted_index[term].append(doc_id)
        occurrences[doc_id][term] = words.count(term)

# All document IDs
all_docs = set(documents.keys())

# Boolean AND
def boolean_and(terms):
    result = set(inverted_index.get(terms[0], []))
    for term in terms[1:]:
        result &= set(inverted_index.get(term, []))
    return result

# Boolean OR
def boolean_or(terms):
    result = set()
    for term in terms:
        result |= set(inverted_index.get(term, []))
    return result

# Boolean NOT
def boolean_not(term):
    return all_docs - set(inverted_index.get(term, []))

# Sample queries
query1 = ["lectures", "bsc"]      # AND
query2 = ["holiday", "lectures"]  # OR
query3 = "lectures"               # NOT

# Results
print("AND Result:", boolean_and(query1))
print("OR Result:", boolean_or(query2))
print("NOT Result:", boolean_not(query3))
