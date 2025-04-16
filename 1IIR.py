# Tiny document retrieval system
docs = [
    "The quick brown fox jumped over the lazy dog",
    "The lazy dog slept in the sun"
]

# Build simple inverted index
index = {}
for i, doc in enumerate(docs):
    for word in doc.lower().split():
        if word not in index:
            index[word] = []
        if i not in index[word]:
            index[word].append(i)

# Print index
print("Index:")
for word in sorted(index):
    print(f"{word}: {', '.join(f'Doc {i+1}' for i in index[word])}")

# Search function
def search(query, and_logic=False):
    words = query.lower().split()
    if and_logic:
        # AND logic - must contain all words
        result = set(range(len(docs)))
        for word in words:
            if word in index:
                result &= set(index[word])
            else:
                return []
    else:
        # OR logic - can contain any word
        result = set()
        for word in words:
            if word in index:
                result |= set(index[word])
    return [docs[i] for i in result]

# Test multiple queries
queries = ["lazy sun", "quick fox", "dog", "brown slept"]
print("\nMultiple Queries:")
for query in queries:
    print(f"\nQuery: '{query}'")
    print("OR results:", search(query))
    print("AND results:", search(query, True))