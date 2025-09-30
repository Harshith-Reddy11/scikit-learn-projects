import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
wine = datasets.load_wine()
X = wine.data
y = wine.target

# Split into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize classifiers
models = {
    "Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(),
    "KNN": KNeighborsClassifier()
}

train_accuracies = []
test_accuracies = []
names = []

# Train, Predict, and Evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    train_acc = accuracy_score(y_train, y_pred_train)
    test_acc = accuracy_score(y_test, y_pred_test)
    
    train_accuracies.append(train_acc)
    test_accuracies.append(test_acc)
    names.append(name)

# Plot comparison
x = range(len(models))
plt.figure(figsize=(8,5))
plt.bar(x, train_accuracies, width=0.4, label="Training Accuracy", align="center")
plt.bar([p+0.4 for p in x], test_accuracies, width=0.4, label="Testing Accuracy", align="center")
plt.xticks([p+0.2 for p in x], names)
plt.ylabel("Accuracy")
plt.title("Wine Dataset Classifiers: Train vs Test Accuracy")
plt.legend()
plt.savefig("wine_classifiers_comparison.png")
plt.show()
