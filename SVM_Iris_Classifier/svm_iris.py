import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

# Load dataset (only 2 features for visualization)
iris = datasets.load_iris()
X = iris.data[:, :2]   # take sepal length and sepal width
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train SVM
svm = SVC(kernel='linear', C=1.0)
svm.fit(X_train, y_train)

# Predictions
y_pred = svm.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("SVM Accuracy:", acc)

# -------- Visualization --------
# Create mesh grid
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# Predict over mesh grid
Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, marker="o", label="Train")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker="x", label="Test")
plt.title("SVM Decision Boundaries on Iris Dataset")
plt.xlabel("Sepal Length (scaled)")
plt.ylabel("Sepal Width (scaled)")
plt.legend()
plt.savefig("svm_decision_boundaries.png")
plt.show()
