from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Define models
models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "SVM": SVC(kernel='linear')
}

# Cross-validation setup
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Store results
results = {}

for name, model in models.items():
    cv_scores = cross_val_score(model, X, y, cv=kfold)
    results[name] = cv_scores
    print(f"{name} CV Scores: {cv_scores}")
    print(f"{name} Mean Accuracy: {cv_scores.mean():.4f}")

# Visualization
plt.boxplot(results.values(), tick_labels=results.keys())
plt.title("Model Comparison using 5-Fold Cross-Validation")
plt.ylabel("Accuracy")
plt.grid(True)
plt.savefig("cv_results.png")
plt.show()
