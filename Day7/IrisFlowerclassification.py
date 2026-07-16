import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
data = pd.read_csv("iris.csv")

print(data[92:])
print(data.info())

print(data.shape)


print(data["species"].value_counts())


x = data[["sepal_length","sepal_width","petal_length","petal_width"]]
y = data["species"]

e = LabelEncoder()

y = e.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.20,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

modelPred = model.predict(X_test)

print("\nPredictions")
print(modelPred)

accuracy = accuracy_score(y_test, modelPred)

precision = precision_score(
    y_test,
    modelPred,
    average="weighted"
)

recall = recall_score(
    y_test,
    modelPred,
    average="weighted"
)

f1 = f1_score(
    y_test,
    modelPred,
    average="weighted"
)

cm = confusion_matrix(
    y_test,
    modelPred
)

print("\nAccuracy :", accuracy)
print("Precision :", precision)
print("Recall :", recall)
print("F1 Score :", f1)

print("\nConfusion Matrix")

print(cm)


actualReslt = e.inverse_transform(y_test)

predictedResult = e.inverse_transform(modelPred)


comp = pd.DataFrame({
    "ACTUAL" : actualReslt,
    "PREDICTED ": predictedResult
})
print("\nSample Predictions\n")

print(comp.head(12))

ConfusionMatrixDisplay.from_predictions(
    y_test,
    modelPred,
    display_labels=e.classes_
)

plt.title("CONFUSION MATRIX  ")

plt.savefig("confusionMatrix.png")
plt.show()