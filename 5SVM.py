# # Minimal Naive Bayes text classifier for flu prediction
# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB

# # 1. Load data
# train = pd.read_csv("Dataset.csv")
# test = pd.read_csv("Test.csv")

# # 2. Create features by combining text values
# X_train = (train["covid"] + " " + train["fever"])
# y_train = train['flu'].map({'yes': 1, 'no': 0})  # Convert to binary

# # 3. Train model
# vectorizer = CountVectorizer()
# X_train_vec = vectorizer.fit_transform(X_train)
# clf = MultinomialNB().fit(X_train_vec, y_train)

# # 4. Make predictions
# X_test = (test["covid"] + " " + test["fever"])
# X_test_vec = vectorizer.transform(X_test)
# predictions = clf.predict(X_test_vec)

# # 5. Output results
# print(f"Processed {len(test)} test cases:")
# for i, pred in enumerate(predictions):
#     print(f"Case {i+1}: {'Positive' if pred == 1 else 'Negative'}")

# # 6. Save predictions to file
# test['predicted_flu'] = ["yes" if p == 1 else "no" for p in predictions]
# test.to_csv("predictions.csv", index=False)


# Text classification with Naive Bayes and SVM - Simplified
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# Common vectorizer for both models
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)

# Part A: Naive Bayes for binary classification
categories_a = ['rec.sport.baseball', 'sci.med']
train_a = fetch_20newsgroups(subset='train', categories=categories_a, shuffle=True)
test_a = fetch_20newsgroups(subset='test', categories=categories_a, shuffle=True)

# Part B: SVM for multi-class classification
categories_b = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
train_b = fetch_20newsgroups(subset='train', categories=categories_b, shuffle=True)
test_b = fetch_20newsgroups(subset='test', categories=categories_b, shuffle=True)

# Function to train and evaluate a model
def evaluate_model(classifier, train_data, test_data, categories, model_name):
    # Prepare data
    X_train = vectorizer.fit_transform(train_data.data)
    X_test = vectorizer.transform(test_data.data)
    
    # Train and predict
    classifier.fit(X_train, train_data.target)
    predictions = classifier.predict(X_test)
    
    # Evaluate
    accuracy = accuracy_score(test_data.target, predictions)
    report = classification_report(test_data.target, predictions, target_names=categories)
    
    # Print results
    print(f"\n{model_name} Classification")
    print(f"Categories: {categories}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Classification Report:\n{report}")

# Run evaluations
evaluate_model(MultinomialNB(), train_a, test_a, categories_a, "Part A: Naive Bayes")
evaluate_model(LinearSVC(), train_b, test_b, categories_b, "Part B: SVM")
