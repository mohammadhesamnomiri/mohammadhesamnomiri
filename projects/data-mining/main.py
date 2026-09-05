import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def make_dataset(n=500):
    rng = np.random.default_rng(7)
    age = rng.integers(15, 70, n)
    income = rng.normal(2500, 900, n).clip(500, 7000)
    visits = rng.poisson(8, n).clip(1, 30)
    score = 0.0007 * income + 0.15 * visits - 0.015 * age
    target = (score > np.median(score)).astype(int)
    return pd.DataFrame({"age": age, "income": income, "visits": visits, "target": target})


def main():
    df = make_dataset().dropna()
    features = ["age", "income", "visits"]
    X = df[features]
    y = df["target"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    clustering = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = clustering.fit_predict(X_scaled)
    print("K-Means silhouette score:", round(silhouette_score(X_scaled, labels), 3))
    print("Cluster sizes:")
    print(pd.Series(labels).value_counts().sort_index())

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Classifier accuracy:", round(accuracy_score(y_test, pred), 3))


if __name__ == "__main__":
    main()
