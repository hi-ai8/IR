from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score

# True labels (y_true) and predicted probabilities (y_scores)
y_true = [0, 1, 1, 0, 1]
y_scores = [0.1, 0.8, 0.6, 0.3, 0.9]

# Convert probabilities to binary predictions (y_pred) using threshold of 0.5
y_pred = [1 if score >= 0.5 else 0 for score in y_scores]

# Precision, Recall, F1-score
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Average Precision (AP)
avg_precision = average_precision_score(y_true, y_scores)

# Output the results
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Average Precision: {avg_precision:.4f}")
