import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

x = df

wcss = []

for i in range(1, 11):
    model = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    model.fit(x)

    wcss.append(model.inertia_)

plt.figure(figsize=(8,5))

plt.plot(
    range(1,11),
    wcss,
    marker="o"
)

plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")

plt.grid(True)

plt.savefig("graphs/elbow_method.png")

plt.show()

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(x)

plt.figure(figsize=(8,5))

plt.scatter(
    df.iloc[:,0],
    df.iloc[:,1],
    c=df["Cluster"]
)

plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])

plt.title("K-Means Clusters")

plt.savefig("graphs/kmeans_clusters.png")

plt.show()