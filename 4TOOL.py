# # Calculate Average Precision for IR system evaluation
# from sklearn.metrics import average_precision_score

# # Data: 1 = relevant document, 0 = irrelevant document
# actual = [0, 1, 1, 0, 1, 1]  # Ground truth relevance 
# scores = [0.1, 0.4, 0.35, 0.8, 0.65, 0.9]  # Model's confidence scores

# # Calculate Average Precision (area under PR curve)
# ap = average_precision_score(actual, scores)

# # Display result
# print(f'Average Precision: {ap:.3f}')


# IR evaluation metrics using scikit-learn
from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score

# Given data
y_true = [0, 1, 1, 0, 1]  # True labels
y_scores = [0.1, 0.8, 0.6, 0.3, 0.9]  # Predicted scores

# Convert scores to binary predictions (threshold = 0.5)
y_pred = [1 if score >= 0.5 else 0 for score in y_scores]

# Calculate metrics
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
ap = average_precision_score(y_true, y_scores)

# Display results
print(f"Predictions: {y_pred}")
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1-score: {f1:.3f}")
print(f"Average Precision: {ap:.3f}")