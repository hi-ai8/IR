import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import ndcg_score

# Example data with features and relevance scores
X = np.array([
    [0.2, 0.8, 0.5],  
    [0.6, 0.4, 0.7],  
    [0.9, 0.1, 0.3],  
    [0.3, 0.7, 0.9]
])
y = np.array([3, 1, 4, 2])  # Relevance scores

# Create training data for pairwise ranking
def create_pairwise_data(X, y):
    X_diff = []
    y_diff = []
    
    for i in range(len(y)):
        for j in range(i+1, len(y)):
            if y[i] != y[j]:  # Only compare different relevance scores
                X_diff.append(X[i] - X[j])
                y_diff.append(np.sign(y[i] - y[j]))
                
    return np.array(X_diff), np.array(y_diff)

# Train and evaluate
X_train, y_train = create_pairwise_data(X, y)
model = LinearSVC()
model.fit(X_train, y_train)

# Get ranking scores and evaluate
scores = model.decision_function(X)
print(f"NDCG Score: {ndcg_score([y], [scores]):.4f}")
