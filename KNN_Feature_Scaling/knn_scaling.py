from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# -------- Without Scaling --------
knn_no_scaling = KNeighborsClassifier(n_neighbors=5)
knn_no_scaling.fit(X_train, y_train)
y_pred_no_scaling = knn_no_scaling.predict(X_test)
acc_no_scaling = accuracy_score(y_test, y_pred_no_scaling)

# -------- With Scaling --------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_scaling = KNeighborsClassifier(n_neighbors=5)
knn_scaling.fit(X_train_scaled, y_train)
y_pred_scaling = knn_scaling.predict(X_test_scaled)
acc_scaling = accuracy_score(y_test, y_pred_scaling)

# Print results
print("KNN without scaling accuracy:", acc_no_scaling)
print("KNN with scaling accuracy:", acc_scaling)

# -------- Visualization --------
plt.figure(figsize=(6,4))
plt.bar(["Without Scaling", "With Scaling"], [acc_no_scaling, acc_scaling], color=["red", "green"])
plt.title("Effect of Feature Scaling on KNN")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.savefig("knn_scaling_comparison.png")
plt.show()
