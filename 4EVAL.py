# # Simple IR metrics calculator
# def ir_metrics(retrieved, relevant):
#     """Calculate precision, recall and F1 score"""
#     # Find intersections and differences
#     tp = len(retrieved & relevant)   # True positives
#     fp = len(retrieved - relevant)   # False positives
#     fn = len(relevant - retrieved)   # False negatives
    
#     # Calculate metrics
#     prec = tp / (tp + fp) if (tp + fp) > 0 else 0
#     rec = tp / (tp + fn) if (tp + fn) > 0 else 0
#     f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
    
#     return prec, rec, f1

# # Example
# docs_retrieved = {"doc1", "doc2", "doc3"}  # System returned these
# docs_relevant = {"doc1", "doc4"}           # Actually relevant

# # Calculate metrics
# p, r, f = ir_metrics(docs_retrieved, docs_relevant)

# # Display results
# print(f"TP: {len(docs_retrieved & docs_relevant)}, " 
#       f"FP: {len(docs_retrieved - docs_relevant)}, "
#       f"FN: {len(docs_relevant - docs_retrieved)}")
# print(f"Precision: {p:.2f}, Recall: {r:.2f}, F1: {f:.2f}")


# IR metrics calculator with fixed values
# Given values
tp = 20  # True positives
fp = 10  # False positives
fn = 30  # False negatives

# Calculate metrics
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f_measure = 2 * (precision * recall) / (precision + recall)

# Display results
print(f"True Positives: {tp}")
print(f"False Positives: {fp}")
print(f"False Negatives: {fn}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F-measure: {f_measure:.4f}")