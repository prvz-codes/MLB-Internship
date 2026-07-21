import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
iris = load_iris()
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

plt.figure(figsize=(8,5))
plt.scatter(
    df.iloc[:,0],
    df.iloc[:,1]
)
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.title("Original Data")
plt.savefig("graphs/original_data.png")
plt.show()
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = model.fit_predict(df)

plt.figure(figsize=(8,5))

plt.scatter(
    df.iloc[:,0],
    df.iloc[:,1],
    c=clusters
)

plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.title("K-Means Clustering")
plt.savefig("graphs/kmeans_clusters.png")
plt.show()

pca = PCA(n_components=2)

new_data = pca.fit_transform(df)

result = pd.DataFrame(
    new_data,
    columns=["PC1","PC2"]
)

result["Cluster"] = clusters

plt.figure(figsize=(8,5))

plt.scatter(
    result["PC1"],
    result["PC2"],
    c=result["Cluster"]
)

plt.title("PCA with K-Means")

plt.xlabel("PC1")
plt.ylabel("PC2")

plt.savefig("graphs/pca_vs_kmeans.png")

plt.show()

print("\nObservation")
print("Clusters Formed : 3")
print("The clusters closely match the 3  Iris flower species  ")
print("PCA reduced four features into two principal components ")