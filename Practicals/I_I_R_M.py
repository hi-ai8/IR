# Input documents
document1 = "best of luck tycs students for your practical examination."
document2 = "tycs students please carry your journal at the time of practical examination."

# Tokenize and preprocess the documents (convert to lowercase and split into words)
tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

# Initialize an empty inverted index and document occurrence dictionary
inverted_index = {}
occurrences = {"Document 1": {}, "Document 2": {}}

# Build inverted index and count occurrences of each term in the documents
for term in set(tokens1 + tokens2):
    inverted_index[term] = []
    
    # If the term is in Document 1, add it to the inverted index
    if term in tokens1:
        inverted_index[term].append("Document 1")
        occurrences["Document 1"][term] = tokens1.count(term)
    
    # If the term is in Document 2, add it to the inverted index
    if term in tokens2:
        inverted_index[term].append("Document 2")
        occurrences["Document 2"][term] = tokens2.count(term)

# Print the inverted index
print("Inverted Index:")
for term, docs in inverted_index.items():
    print(f"{term} -> {', '.join(docs)}")

# Function to search for documents containing specific terms
def search(terms):
    # Use set to avoid duplicates and return documents containing the terms
    results = set()
    for term in terms:
        if term in inverted_index:
            results.update(inverted_index[term])
    return results

# Search for documents containing the terms "tycs" and "journal"
search_result = search(["tycs", "journal"])

# Print the results of the search
print("\nDocuments containing the terms 'tycs' and 'journal':")
print(", ".join(search_result))
