import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Perform hierarchical clustering (ward method = minimize variance)
Z = linkage(X, method='ward')

# Plot dendrogram
plt.figure(figsize=(10, 6))
dendrogram(Z, truncate_mode="level", p=5)
plt.title("Iris Dataset Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.savefig("iris_dendrogram.png")
plt.show()

# Cut dendrogram at 3 clusters
clusters = fcluster(Z, t=3, criterion="maxclust")

# Reduce to 2D for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot clusters
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:,0], X_pca[:,1], c=clusters, cmap="viridis", s=50)
plt.title("Hierarchical Clustering on Iris Dataset")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.savefig("iris_clusters.png")
plt.show()
