import pandas as p

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (    accuracy_score,    precision_score,    recall_score,    f1_score,    confusion_matrix,    classification_report
                            )

from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
data = load_breast_cancer()



df = p.DataFrame(data.data , columns = data.feature_names)

df["target"] = data.target

print(df.head())
print(df.info())

print(df.describe())

x  = data.data
y = data.target

x_train  , x_test ,y_train , y_test = train_test_split(
    x , y , test_size=0.2, random_state=42
)

scalar = StandardScaler()
x_train = scalar.fit_transform(x_train)
x_test = scalar.transform(x_test)

model = LogisticRegression(max_iter=5000)

model.fit(x_train , y_train)
modelPred = model.predict(x_test)
print("Accuracy :", accuracy_score(y_test, modelPred))
print("Precision:", precision_score(y_test, modelPred))
print("Recall   :", recall_score(y_test, modelPred))
print("F1 Score :", f1_score(y_test, modelPred))

print(confusion_matrix(y_test , modelPred))
print(classification_report(y_test, modelPred))

param  = {
    "C" : [0.01 , 0.1 , 1 , 10 , 100],
     "solver": ["liblinear", "lbfgs"]
}

gridSearch = GridSearchCV(
    LogisticRegression(max_iter=5000),
    param ,
    cv=5,
    scoring="accuracy"
)
gridSearch.fit(x_train , y_train)

print(gridSearch.best_params_)

best_model = gridSearch.best_estimator_

tuned_predictions = best_model.predict(x_test)

print("\n Tuned Model \n")


print("Accuracy :", accuracy_score(y_test, tuned_predictions))
print("Precision:", precision_score(y_test, tuned_predictions))
print("Recall   :", recall_score(y_test, tuned_predictions))
print("F1 Score :", f1_score(y_test, tuned_predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, tuned_predictions))

print("\nClassification Report")
print(classification_report(y_test, tuned_predictions))


print(f"Baseline Accuracy : {accuracy_score(y_test, modelPred):.4f}")
print(f"Tuned Accuracy    : {accuracy_score(y_test, tuned_predictions):.4f}")

print(f"Baseline Precision: {precision_score(y_test, modelPred):.4f}")
print(f"Tuned Precision   : {precision_score(y_test, tuned_predictions):.4f}")

print(f"Baseline Recall   : {recall_score(y_test, modelPred):.4f}")
print(f"Tuned Recall      : {recall_score(y_test, tuned_predictions):.4f}")

print(f"Baseline F1 Score : {f1_score(y_test, modelPred):.4f}")
print(f"Tuned F1 Score    : {f1_score(y_test, tuned_predictions):.4f}")

ConfusionMatrixDisplay.from_estimator(
    best_model,
    x_test,
    y_test
)

plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.show()