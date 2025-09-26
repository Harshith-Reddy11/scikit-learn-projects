# Day 1 - Iris Flower Classification with Scikit-learn

# Step 1: Import libraries
from sklearn.datasets import load_iris                # To load the iris dataset
from sklearn.model_selection import train_test_split  # To split dataset into train & test
from sklearn.linear_model import LogisticRegression   # Our ML algorithm (Logistic Regression)
from sklearn.metrics import accuracy_score            # To check how good our model is

# Step 2: Load dataset
iris = load_iris()           # iris is a dictionary-like object with data & labels
X = iris.data                # Features (sepal length, sepal width, petal length, petal width)
y = iris.target              # Labels (0 = Setosa, 1 = Versicolor, 2 = Virginica)

# Step 3: Split data into train & test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# test_size=0.2 → 20% data for testing, 80% for training
# random_state=42 → makes sure results are reproducible

# Step 4: Train model
model = LogisticRegression(max_iter=200)  # Create model (max_iter=200 helps avoid warnings)
model.fit(X_train, y_train)               # Train the model on training data

# Step 5: Predictions
y_pred = model.predict(X_test)  # Model makes predictions on test data

# Step 6: Evaluate
accuracy = accuracy_score(y_test, y_pred)  # Compare predictions with actual labels
print("Model Accuracy:", accuracy)

# Step 7: Test on custom input
sample = [[5.1, 3.5, 1.4, 0.2]]  # Example measurements of a flower
prediction = model.predict(sample)  # Predict flower type
print("Prediction for sample:", iris.target_names[prediction][0])
