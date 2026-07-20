import pandas as p
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

data = load_breast_cancer()

df = p.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

print(df.head())
print(df.info())
print(df.describe())

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

baselineModel = LogisticRegression(max_iter=5000)
baselineModel.fit(x_train, y_train)
baselinePrediction = baselineModel.predict(x_test)
print("\nBaseline Model\n")
print("Accuracy :", accuracy_score(y_test, baselinePrediction))
print("Precision:", precision_score(y_test, baselinePrediction))
print("Recall   :", recall_score(y_test, baselinePrediction))
print("F1 Score :", f1_score(y_test, baselinePrediction))
print("\nConfusion Matrix")
print(confusion_matrix(y_test, baselinePrediction))
print("\nClassification Report")
print(classification_report(y_test, baselinePrediction))

param = {
    "C": [0.01, 0.1, 1, 10, 100],
    "solver": ["liblinear", "lbfgs"]
}



gridSearch = GridSearchCV(
    LogisticRegression(max_iter=5000),
    param,
    cv=5,
    scoring="accuracy"
)

gridSearch.fit(x_train, y_train)

print("\nBest Parameters")
print(gridSearch.best_params_)
bestModel = gridSearch.best_estimator_
tunedPrediction = bestModel.predict(x_test)



print("\nTuned Model\n")
print("Accuracy :", accuracy_score(y_test, tunedPrediction))
print("Precision:", precision_score(y_test, tunedPrediction))
print("Recall   :", recall_score(y_test, tunedPrediction))
print("F1 Score :", f1_score(y_test, tunedPrediction))
print("\nConfusion Matrix")
print(confusion_matrix(y_test, tunedPrediction))
print("\nClassification Report")
print(classification_report(y_test, tunedPrediction))




metricNames = ["Accuracy", "Precision", "Recall", "F1-Score"]
baselineScores = [
    accuracy_score(y_test, baselinePrediction),
    precision_score(y_test, baselinePrediction),
    recall_score(y_test, baselinePrediction),
    f1_score(y_test, baselinePrediction)
]
tunedScores = [
    accuracy_score(y_test, tunedPrediction),
    precision_score(y_test, tunedPrediction),
    recall_score(y_test, tunedPrediction),
    f1_score(y_test, tunedPrediction)
]
xPosition = [0, 1, 2, 3]
barWidth = 0.35
plt.figure(figsize=(8, 5))
plt.bar(
    [i - barWidth / 2 for i in xPosition],
    baselineScores,
    width=barWidth,
    label="Baseline Model"
)
plt.bar(
    [i + barWidth / 2 for i in xPosition],
    tunedScores,
    width=barWidth,
    label="Tuned Model"
)
plt.xticks(xPosition, metricNames)
plt.xlabel("Evaluation Metrics")
plt.ylabel("Score")
plt.title("Baseline vs Tuned Model")
plt.ylim(0.90, 1.00)
plt.legend()
plt.savefig("baseline_vs_tuned.png")
plt.show()



ConfusionMatrixDisplay.from_estimator(
    bestModel,
    x_test,
    y_test
)




plt.title("Breast Cancer Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.show()
print("\nSample Predictions\n")
samplePrediction = bestModel.predict(x_test[:5])
for i in range(5):
    actual = "Benign" if y_test[i] == 1 else "Malignant"
    predicted = "Benign" if samplePrediction[i] == 1 else "Malignant"
    print("Patient", i + 1)
    print("Actual    :", actual)
    print("Predicted :", predicted)
    print("-" * 30)