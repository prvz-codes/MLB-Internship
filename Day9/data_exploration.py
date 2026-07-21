import pandas as pd

from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["Species"] = iris.target
print("\nFirst Five Rows")
print(df.head())
print("\nDataset Information")
print(df.info())
print("\nStatistical Summary")
print(df.describe())
print("\nMissing Values")
print(df.isnull().sum())
print("\nSpecies Count")
print(df["Species"].value_counts())