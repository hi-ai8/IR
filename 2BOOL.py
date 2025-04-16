# Minimal Boolean retrieval system with AND, OR, NOT
docs = {1: "BSc lectures start at 7", 
        2: "My lectures are over", 
        3: "Today is a holiday"}

# Build index
idx = {}
for id, doc in docs.items():
    for word in doc.lower().split():
        if word not in idx: idx[word] = set()
        idx[word].add(id)

# Print index
print("Index:")
for term in sorted(idx):
    print(f"{term}: {sorted(idx[term])}")

# Process queries
all_docs = set(docs.keys())

# NOT query
not_term = "lectures"
not_result = all_docs - idx.get(not_term, set())
print(f"\nQuery: 'NOT {not_term}'")
print(f"Results: {sorted(not_result)}")

# # AND query
# and_terms = ["lectures", "start"]
# and_result = all_docs
# for term in and_terms:
#     and_result &= idx.get(term, set())
# print(f"\nQuery: '{' AND '.join(and_terms)}'")
# print(f"Results: {sorted(and_result)}")

# # OR query
# or_terms = ["lectures", "holiday"]
# or_result = set()
# for term in or_terms:
#     or_result |= idx.get(term, set())
# print(f"\nQuery: '{' OR '.join(or_terms)}'")
# print(f"Results: {sorted(or_result)}")

# Print matching documents for all queries
print("\nMatching documents:")
for query, result in [("NOT lectures", not_result)]: 
                    #   ("lectures AND start", and_result),
                    #   ("lectures OR holiday", or_result)]:
    print(f"\n'{query}':")
    for id in sorted(result):
        print(f"  Doc {id}: {docs[id]}")