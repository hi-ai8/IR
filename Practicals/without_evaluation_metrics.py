# Given values for TP, FP, FN
TP = 20
FP = 10
FN = 30

# Calculate Precision, Recall, and F-Score manually
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1_score = 2 * (precision * recall) / (precision + recall)

# Output the results
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F-Score: {f1_score:.4f}")
