import pandas as p

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (    accuracy_score,    precision_score,    recall_score,    f1_score,    confusion_matrix,    classification_report
                            )

data = load_breast_cancer()



df = p.DataFrame(data.data , columns = data.feature_names)

df["taget"] = data.target

x  = data.data
y = data.target

x_train  , x_test ,y_train , y_test = train_test_split(
    x , y , test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=5000)

model.fit(x_train , y_train)
modelPred = model.predict(x_test)
print("Accuracy :", accuracy_score(y_test, modelPred))
print("Precision:", precision_score(y_test, modelPred))
print("Recall   :", recall_score(y_test, modelPred))
print("F1 Score :", f1_score(y_test, modelPred))

print(confusion_matrix(y_test , modelPred))
print(classification_report(y_test, modelPred))
