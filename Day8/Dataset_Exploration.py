import pandas as p

from sklearn.datasets import load_breast_cancer


data = load_breast_cancer()


df = p.DataFrame(data.data , columns = data.feature_names)

df["taget"] = data.target

print(df.head())
print(df.info())

print(df.describe())
