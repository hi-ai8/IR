import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import ndcg_score

# Example data
X = np.array([[0.2, 0.8, 0.5], [0.6, 0.4, 0.7], [0.9, 0.1, 0.3], [0.3, 0.7, 0.9]])
y = np.array([3, 1, 4, 2])

# Pairwise comparison for RankSVM
pairs = [(i, j) for i in range(len(y)) for j in range(i + 1, len(y))]
X_train = np.array([X[i] - X[j] if y[i] > y[j] else X[j] - X[i] for i, j in pairs])
y_train = np.array([1 if y[i] > y[j] else -1 for i, j in pairs])

# Train RankSVM
rank_svm = SVC(kernel="linear").fit(X_train, y_train)

# Predict and evaluate with NDCG
y_pred = rank_svm.decision_function(X)
print("NDCG Score:", ndcg_score([y], [y_pred]))
