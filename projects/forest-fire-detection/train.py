from pathlib import Path
import numpy as np
import pandas as pd
from joblib import dump
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "fire_risk.csv"
MODEL_DIR = ROOT / "models"


def make_demo_dataset(path: Path, n: int = 600) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    temperature = rng.normal(31, 7, n).clip(10, 50)
    humidity = rng.normal(42, 18, n).clip(5, 95)
    wind = rng.normal(16, 8, n).clip(0, 45)
    rain = rng.exponential(2.0, n).clip(0, 20)
    score = 0.11 * temperature + 0.055 * wind - 0.045 * humidity - 0.12 * rain
    risk = (score + rng.normal(0, 1.0, n) > 1.7).astype(int)
    df = pd.DataFrame({"temperature": temperature, "humidity": humidity,
                       "wind": wind, "rain": rain, "risk": risk})
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return df


def load_data() -> pd.DataFrame:
    if DATA.exists():
        return pd.read_csv(DATA)
    return make_demo_dataset(DATA)


def main() -> None:
    df = load_data().dropna()
    features = ["temperature", "humidity", "wind", "rain"]
    X, y = df[features], df["risk"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "SVM": Pipeline([("scale", StandardScaler()), ("model", SVC(kernel="rbf"))]),
        "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
    }
    best_name, best_model, best_score = None, None, -1
    for name, model in models.items():
        model.fit(X_train, y_train)
        score = accuracy_score(y_test, model.predict(X_test))
        print(f"{name}: accuracy={score:.3f}")
        if score > best_score:
            best_name, best_model, best_score = name, model, score

    predictions = best_model.predict(X_test)
    print(f"\nBest model: {best_name}")
    print(classification_report(y_test, predictions, zero_division=0))
    MODEL_DIR.mkdir(exist_ok=True)
    dump(best_model, MODEL_DIR / "fire_risk_model.joblib")
    print(f"Saved model to {MODEL_DIR / 'fire_risk_model.joblib'}")


if __name__ == "__main__":
    main()
