"""Placement prediction service."""

import os
from typing import Any, Dict

import joblib
import numpy as np
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "placement_model.pkl")

_model_cache: Dict[str, Any] = {}


def _load_model() -> Dict[str, Any]:
    if not _model_cache:
        data = joblib.load(MODEL_PATH)
        _model_cache.update(data)
    return _model_cache


def predict_placement(
    cgpa: float,
    aptitude: float,
    programming: float,
    communication: float,
    tenth_percentage: float = 0.0,
    twelfth_percentage: float = 0.0,
    projects: int = 0,
    internships: int = 0,
) -> Dict[str, Any]:
    """Predict placement probability based on the trained model."""

    MIN_CGPA = 6.5
    MIN_APTITUDE = 50
    MIN_PROGRAMMING = 40
    MIN_COMMUNICATION = 45
    MIN_TENTH = 50
    MIN_TWELFTH = 50

    model_data = _load_model()
    pipeline = model_data["pipeline"]
    base_importances = model_data["feature_importances"]

    input_df = pd.DataFrame([
        {
            "cgpa": cgpa,
            "aptitude": aptitude,
            "programming": programming,
            "communication": communication,
            "tenth_percentage": tenth_percentage,
            "twelfth_percentage": twelfth_percentage,
            "projects": projects,
            "internships": internships,
        }
    ])

    warnings = []
    if cgpa < MIN_CGPA:
        warnings.append(f"CGPA {cgpa} < {MIN_CGPA}")
    if aptitude < MIN_APTITUDE:
        warnings.append(f"Aptitude {aptitude}% < {MIN_APTITUDE}%")
    if programming < MIN_PROGRAMMING:
        warnings.append(f"Programming {programming}% < {MIN_PROGRAMMING}%")
    if communication < MIN_COMMUNICATION:
        warnings.append(f"Communication {communication}% < {MIN_COMMUNICATION}%")
    if tenth_percentage < MIN_TENTH:
        warnings.append(f"10th {tenth_percentage}% < {MIN_TENTH}%")
    if twelfth_percentage < MIN_TWELFTH:
        warnings.append(f"12th {twelfth_percentage}% < {MIN_TWELFTH}%")

    prediction = float(pipeline.predict(input_df)[0])
    placed_prob = round(float(np.clip(prediction, 0.0, 1.0)) * 100.0, 2)

    if placed_prob >= 90:
        confidence = "Elite"
    elif placed_prob >= 75:
        confidence = "Very High"
    elif placed_prob >= 60:
        confidence = "High"
    elif placed_prob >= 45:
        confidence = "Medium"
    elif placed_prob >= 25:
        confidence = "Low"
    else:
        confidence = "Very Low"

    explanation = "⚠️ Improve: " + ", ".join(warnings) if warnings else None

    total = sum(base_importances.values())
    fi_pct = {k: round(v / total * 100, 1) for k, v in base_importances.items()}

    label_map = {
        "cgpa": "CGPA",
        "aptitude": "Aptitude Score",
        "programming": "Programming Skills",
        "communication": "Communication",
        "tenth_percentage": "10th Percentage",
        "twelfth_percentage": "12th Percentage",
        "projects": "Projects",
        "internships": "Internships",
    }
    feature_importance = [
        {"factor": label_map.get(k, k), "contribution": v}
        for k, v in sorted(fi_pct.items(), key=lambda item: -item[1])
    ]

    return {
        "probability": placed_prob,
        "confidence": confidence,
        "feature_importance": feature_importance,
        "placed": placed_prob >= 50,
        "min_requirements": {
            "cgpa": MIN_CGPA,
            "aptitude": MIN_APTITUDE,
            "programming": MIN_PROGRAMMING,
            "communication": MIN_COMMUNICATION,
            "tenth_percentage": MIN_TENTH,
            "twelfth_percentage": MIN_TWELFTH,
        },
        "explanation": explanation,
    }

