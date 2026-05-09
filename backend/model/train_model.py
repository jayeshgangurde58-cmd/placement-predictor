"""
Train and save the placement prediction model.
Run this once: python backend/model/train_model.py
"""

import os

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

SEED = 42
np.random.seed(SEED)
N = 6000


def generate_data(n: int) -> pd.DataFrame:
    """Generate realistic placement data based on company hiring standards."""
    cgpa = np.round(np.random.normal(7.2, 0.9, n).clip(4.0, 10.0), 2)
    aptitude = np.random.randint(40, 100, n).astype(float)
    programming = np.random.randint(30, 100, n).astype(float)
    communication = np.random.randint(40, 100, n).astype(float)
    tenth = np.random.randint(35, 100, n).astype(float)
    twelfth = np.random.randint(35, 100, n).astype(float)
    projects = np.random.randint(0, 6, n).astype(float)
    internships = np.random.randint(0, 4, n).astype(float)

    min_cgpa = 6.5
    min_aptitude = 50
    min_programming = 40
    min_communication = 45
    min_tenth = 50
    min_twelfth = 50

    base_score = (
        cgpa * 2.0
        + aptitude * 0.15
        + programming * 0.25
        + communication * 0.15
        + tenth * 0.06
        + twelfth * 0.06
        + projects * 3.5
        + internships * 4.5
        - 50
    )

    placement_prob = 1 / (1 + np.exp(-0.12 * base_score))
    below_threshold = (
        (cgpa < min_cgpa)
        | (aptitude < min_aptitude)
        | (programming < min_programming)
        | (communication < min_communication)
        | (tenth < min_tenth)
        | (twelfth < min_twelfth)
    )
    placement_prob[below_threshold] *= 0.30
    placement_prob = np.clip(placement_prob + np.random.normal(0, 0.03, n), 0.01, 0.99)

    return pd.DataFrame({
        "cgpa": cgpa,
        "aptitude": aptitude,
        "programming": programming,
        "communication": communication,
        "tenth_percentage": tenth,
        "twelfth_percentage": twelfth,
        "projects": projects,
        "internships": internships,
        "placement_probability": placement_prob,
    })


def train():
    df = generate_data(N)
    X = df.drop("placement_probability", axis=1)
    y = df["placement_probability"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=SEED
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestRegressor(
            n_estimators=250,
            max_depth=14,
            min_samples_leaf=5,
            random_state=SEED,
            max_features="sqrt",
        )),
    ])

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"Model RMSE: {rmse:.4f}")

    feature_names = X.columns.tolist()
    importances = pipeline.named_steps["model"].feature_importances_
    fi_map = {f: round(float(imp), 4) for f, imp in zip(feature_names, importances)}
    print(f"Feature importances: {fi_map}")

    os.makedirs(os.path.dirname(__file__) if os.path.dirname(__file__) else ".", exist_ok=True)
    out_path = os.path.join(os.path.dirname(__file__), "placement_model.pkl")
    joblib.dump({"pipeline": pipeline, "feature_names": feature_names, "feature_importances": fi_map}, out_path)
    print(f"Model saved to {out_path}")


if __name__ == "__main__":
    train()

