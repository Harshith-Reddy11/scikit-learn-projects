import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import numpy as np

# Load dataset (ignore labels for clustering)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Apply KMeans with 3 clusters (since Iris has 3 classes)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
y_pred = kmeans.fit_predict(X)

# Map predicted clusters to actual labels
# (since cluster numbers don't necessarily match label numbers)
labels = np.zeros_like(y_pred)
for i in range(3):
    mask = (y_pred == i)
    labels[mask] = np.bincount(y[mask]).argmax()

# Evaluate clustering accuracy
print("K-Means Clustering Accuracy:", accuracy_score(y, labels))

# Reduce to 2D with PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot clusters
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:,0], X_pca[:,1], c=labels, cmap="viridis", s=50)
plt.title("K-Means Clustering on Iris Dataset")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.savefig("iris_kmeans.png")
plt.show()
