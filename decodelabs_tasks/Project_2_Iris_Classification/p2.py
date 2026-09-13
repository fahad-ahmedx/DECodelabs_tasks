# Project 2: Data Classification Using AI
# DecodeLabs Artificial Intelligence Training

# --------------------------------------------------
# 1. IMPORT LIBRARIES
# --------------------------------------------------

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    f1_score
)

import matplotlib.pyplot as plt


# --------------------------------------------------
# 2. LOAD THE IRIS DATASET
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("=" * 60)
print("       IRIS DATA CLASSIFICATION USING AI")
print("=" * 60)

print("\nDataset Information:")
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Feature names:", iris.feature_names)
print("Classes:", iris.target_names)


# --------------------------------------------------
# 3. SPLIT DATA INTO TRAINING AND TESTING SETS
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    shuffle=True,
    stratify=y
)

print("\nData Split:")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# --------------------------------------------------
# 4. SCALE THE FEATURES
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling completed.")
print("Training data has been standardized.")


# --------------------------------------------------
# 5. CREATE THE K-NEAREST NEIGHBORS MODEL
# --------------------------------------------------

model = KNeighborsClassifier(n_neighbors=5)


# --------------------------------------------------
# 6. TRAIN THE MODEL
# --------------------------------------------------

model.fit(X_train_scaled, y_train)

print("\nKNN model training completed.")
print("Number of neighbors (K): 5")


# --------------------------------------------------
# 7. MAKE PREDICTIONS
# --------------------------------------------------

y_pred = model.predict(X_test_scaled)

print("\nPredictions completed.")


# --------------------------------------------------
# 8. CALCULATE ACCURACY
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")


# --------------------------------------------------
# 9. CONFUSION MATRIX
# --------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# --------------------------------------------------
# 10. F1 SCORE
# --------------------------------------------------

f1 = f1_score(y_test, y_pred, average="weighted")

print("\nWeighted F1 Score:")
print(f"{f1:.4f}")


# --------------------------------------------------
# 11. CLASSIFICATION REPORT
# --------------------------------------------------

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


# --------------------------------------------------
# 12. DISPLAY CONFUSION MATRIX VISUALLY
# --------------------------------------------------

plt.figure(figsize=(7, 5))

plt.imshow(cm)

plt.title("Confusion Matrix - Iris Classification")
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")

plt.xticks(
    range(len(iris.target_names)),
    iris.target_names
)

plt.yticks(
    range(len(iris.target_names)),
    iris.target_names
)

# Display numbers inside the matrix
for i in range(len(cm)):
    for j in range(len(cm[i])):
        plt.text(j, i, cm[i][j], ha="center", va="center")

plt.colorbar()
plt.tight_layout()
plt.show()