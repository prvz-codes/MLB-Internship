import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

pca = PCA(n_components=2)

pca_data = pca.fit_transform(df)

result = pd.DataFrame(
    pca_data,
    columns=["PC1","PC2"]
)

result["Species"] = iris.target

plt.figure(figsize=(8,5))

plt.scatter(
    result["PC1"],
    result["PC2"],
    c=result["Species"]
)

plt.title("PCA Visualization")

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.savefig("graphs/pca_visualization.png")

plt.show()

print("Explained Variance Ratio")

print(pca.explained_variance_ratio_)