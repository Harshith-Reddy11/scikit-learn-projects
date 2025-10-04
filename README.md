# scikit-learn-projects

---

# 🤖 Scikit-Learn Projects

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-green.svg)](https://github.com/your-username/scikit-learn-projects)
[![GitHub Streak](https://img.shields.io/badge/GitHub-Streak-red.svg)](https://gitHub.com/your-username)

---

## 📚 Overview

This repository contains hands-on **Machine Learning projects** built using [Scikit-learn](https://scikit-learn.org/).  
The goal is to learn ML through **project-based learning** and maintain a **daily GitHub streak** 🚀.

---

## 📂 Project List

### 1️⃣ [Iris Classifier](./Iris_Classifier)

- Built a classifier for the famous **Iris dataset** 🌸.
- Trained a **Logistic Regression** to classify flowers.
- Includes an **ML pipeline flowchart** for easy understanding.
- 📊 **Output:** Predicts flower species based on features.

### 2️⃣ [Model Comparison](./Model_Comparison)

- Compared **Logistic Regression, Decision Tree, Random Forest** on the **Iris dataset**.
- Visualized accuracies with a **bar chart**.
- 📊 **Output:** See which algorithm performs best.

### 3️⃣ [KNN Feature Scaling](./KNN_Feature_Scaling)

- Demonstrates the effect of **feature scaling** on **K-Nearest Neighbors (KNN)** accuracy.
- Compares KNN performance with and without scaling using the Iris dataset.
- Includes a **bar chart** visualizing accuracy improvement.
- 📊 **Output:** Shows the importance of scaling for distance-based algorithms.

### 4️⃣ [SVM Iris Classifier](./SVM_Iris_Classifier)

- Implements **Support Vector Machine (SVM)** for classifying the Iris dataset.
- Applies feature scaling and visualizes SVM decision boundaries.
- 📊 **Output:** Shows SVM accuracy and a plot of decision boundaries.

### 5️⃣ [Naive Bayes Classifier – Wine Dataset](./Naive_Bayes_Classifier)

- Demonstrates **Naive Bayes**, **Decision Tree**, and **KNN** classifiers on the Wine dataset.
- Compares training and testing accuracy for each algorithm.
- Includes a **bar chart** visualizing classifier performance.
- 📊 **Output:** Shows which model works best for wine classification.

### 6️⃣ [Digits Classification with PCA & KNN](./Digits_PCA_knn)

- Applies **Principal Component Analysis (PCA)** for dimensionality reduction on the Digits dataset.
- Classifies digits using **K-Nearest Neighbors (KNN)** on PCA-reduced features.
- Visualizes the dataset in 2D using PCA.
- 📊 **Output:** Shows KNN accuracy and a PCA projection plot.

### 7️⃣ [Iris Clustering with K-Means](./Iris_Kmeans)

- Applies **K-Means clustering** to the Iris dataset to group flowers into clusters without labels.
- Maps clusters to actual classes and evaluates clustering accuracy.
- Visualizes clusters using **PCA**.
- 📊 **Output:** Shows clustering accuracy and a PCA-based cluster plot.

### 8️⃣ [Iris Hierarchical Clustering](./Iris_Hierarchical)

- Demonstrates **Hierarchical Clustering** on the Iris dataset.
- Visualizes the clustering process with a dendrogram.
- Displays clusters in 2D space using **PCA**.
- 📊 **Output:** Dendrogram and PCA-based cluster visualization.

---

## 🚀 Getting Started

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/scikit-learn-projects.git
   cd scikit-learn-projects
   ```

2. **Install dependencies:**

   ```sh
   pip install scikit-learn matplotlib graphviz
   ```

3. **Run a project:**
   - Navigate to a project folder (e.g., `Iris_Classifier/`, `Model_Comparison/`, `KNN_Feature_Scaling/`, `SVM_Iris_Classifier/`, `Naive_Bayes_Classifier/`, `Digits_PCA_knn/`, `Iris_Kmeans/`)
   - Run the Python script:
     ```sh
     python iris_classifier.py
     # or
     python model_comparison.py
     # or
     python knn_scaling.py
     # or
     python svm_iris.py
     # or
     python naive_bayes.py
     # or
     python digits_pca_knn.py
     # or
     python iris_kmeans.py
     # or
     python iris_hierarchical.py
     ```

---

## 🗂️ Folder Structure

```
scikit-learn-projects/
│
├── Iris_Classifier/
│   ├── iris_classifier.py
│   ├── iris_ml_pipeline.png
│   └── README.md
│
├── Model_Comparison/
│   ├── model_comparison.py
│   ├── model_comparison.png
│   └── README.md
│
├── KNN_Feature_Scaling/
│   ├── knn_scaling.py
│   ├── knn_scaling_comparison.png
│   └── README.md
│
├── SVM_Iris_Classifier/
│   ├── svm_iris.py
│   ├── svm_decision_boundaries.png
│   └── README.md
│
├── Naive_Bayes_Classifier/
│   ├── naive_bayes.py
│   ├── wine_classifiers_comparison.png
│   └── README.md
│
├── Digits_PCA_knn/
│   ├── digits_pca_knn.py
│   ├── digits_pca.png
│   └── README.md
│
├── Iris_Kmeans/
│   ├── iris_kmeans.py
│   ├── iris_kmeans.png
│   └── README.md
│
├── Iris_Hierarchical/
│   ├── iris_hierarchical.py
│   ├── iris_dendrogram.png
│   ├── iris_clusters.png
│   └── README.md
│
└── README.md
```

---

## 🎯 Learning Roadmap

- **Day 1:** Built first classifier (Iris dataset).
- **Day 2:** Compared ML models.
- **Day 3:** Explored feature scaling with KNN.
- **Day 4:** Implemented SVM with decision boundary visualization.
- **Day 5:** Compared classifiers on the Wine dataset.
- **Day 6:** Applied PCA and KNN on the Digits dataset.
- **Day 7:** Performed clustering with K-Means on Iris dataset.
- **Day 8:** Explored hierarchical clustering and dendrograms.
- **Next:** More datasets, advanced models, and visualizations coming soon!

---

## 📝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy Learning! 🌟
