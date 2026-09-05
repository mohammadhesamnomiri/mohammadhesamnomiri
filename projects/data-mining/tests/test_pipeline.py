from pathlib import Path
import sys

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

sys.path.insert(0, str(Path(__file__).parents[1]))
from main import make_dataset  # noqa: E402


def test_dataset_schema_and_size():
    df = make_dataset(200)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["age", "income", "visits", "target"]
    assert len(df) == 200
    assert df.isna().sum().sum() == 0


def test_clustering_pipeline():
    df = make_dataset(300)
    X = StandardScaler().fit_transform(df[["age", "income", "visits"]])
    labels = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X)
    assert len(set(labels)) == 3
    assert silhouette_score(X, labels) > 0


def test_classifier_pipeline():
    df = make_dataset(300)
    X = StandardScaler().fit_transform(df[["age", "income", "visits"]])
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)
    assert 0 <= accuracy_score(y_test, model.predict(X_test)) <= 1
