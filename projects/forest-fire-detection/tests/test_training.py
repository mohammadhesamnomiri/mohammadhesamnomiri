from pathlib import Path
import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

sys.path.insert(0, str(Path(__file__).parents[1]))
from train import load_data, make_demo_dataset  # noqa: E402


def test_demo_dataset_schema(tmp_path):
    path = tmp_path / "fire_risk.csv"
    df = make_demo_dataset(path, n=120)
    assert path.exists()
    assert list(df.columns) == ["temperature", "humidity", "wind", "rain", "risk"]
    assert len(df) == 120
    assert set(df["risk"].unique()).issubset({0, 1})


def test_loaded_data_is_numeric():
    df = load_data().dropna()
    features = ["temperature", "humidity", "wind", "rain"]
    assert all(pd.api.types.is_numeric_dtype(df[c]) for c in features)
    assert df["risk"].isin([0, 1]).all()


def test_dataset_supports_stratified_split():
    df = load_data().dropna()
    X = df[["temperature", "humidity", "wind", "rain"]]
    y = df["risk"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    assert len(X_train) + len(X_test) == len(df)
    assert len(y_train) == len(X_train)
    assert len(y_test) == len(X_test)
