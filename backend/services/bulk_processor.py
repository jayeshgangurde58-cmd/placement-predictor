"""Bulk CSV analysis service."""

import io
import pandas as pd
from typing import List, Dict, Any

from services.predictor import predict_placement
from services.skill_gap import analyze_skill_gap, get_available_roles

REQUIRED_COLUMNS = {"name", "cgpa", "aptitude", "programming", "communication", "projects", "internships"}
OPTIONAL_COLUMNS = {"skills", "target_role", "tenth_percentage", "twelfth_percentage"}
OPTIONAL_SKILL_COL = "skills"


def process_bulk_csv(file_bytes: bytes, filename: str) -> Dict[str, Any]:
    """Process a CSV file of students and return per-student placement predictions."""
    try:
        df = pd.read_csv(io.BytesIO(file_bytes))
    except Exception as e:
        return {"error": f"Could not parse CSV: {str(e)}"}

    # Normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    missing_cols = REQUIRED_COLUMNS - set(df.columns)
    if missing_cols:
        return {"error": f"Missing required columns: {missing_cols}. Required: {REQUIRED_COLUMNS}"}

    results = []
    errors = []

    for idx, row in df.iterrows():
        try:
            student_name = str(row.get("name", f"Student {idx + 1}"))
            cgpa = float(row["cgpa"])
            aptitude = float(row["aptitude"])
            programming = float(row["programming"])
            communication = float(row["communication"])
            projects = int(row["projects"])
            internships = int(row["internships"])
            tenth_percentage = float(row["tenth_percentage"]) if "tenth_percentage" in df.columns and pd.notna(row.get("tenth_percentage")) else 0.0
            twelfth_percentage = float(row["twelfth_percentage"]) if "twelfth_percentage" in df.columns and pd.notna(row.get("twelfth_percentage")) else 0.0

            prediction = predict_placement(
                cgpa,
                aptitude,
                programming,
                communication,
                tenth_percentage,
                twelfth_percentage,
                projects,
                internships,
            )

            result = {
                "row": idx + 1,
                "name": student_name,
                "cgpa": cgpa,
                "aptitude": aptitude,
                "programming": programming,
                "communication": communication,
                "tenth_percentage": tenth_percentage,
                "twelfth_percentage": twelfth_percentage,
                "projects": projects,
                "internships": internships,
                "probability": prediction["probability"],
                "placed": prediction["placed"],
                "confidence": prediction["confidence"],
            }

            # Optional: parse skills for skill gap
            if OPTIONAL_SKILL_COL in df.columns and pd.notna(row.get(OPTIONAL_SKILL_COL)):
                raw_skills = str(row[OPTIONAL_SKILL_COL])
                skills_list = [s.strip() for s in raw_skills.split(";") if s.strip()]
                # Default to Web Developer if role not specified
                target_role = str(row.get("target_role", "Web Developer"))
                if target_role not in get_available_roles():
                    target_role = "Web Developer"
                gap = analyze_skill_gap(skills_list, target_role)
                result["skill_gap"] = {
                    "target_role": target_role,
                    "match_rate": gap.get("match_rate", 0),
                    "skill_gap_index": gap.get("skill_gap_index", 1),
                    "missing_skills": gap.get("missing_skills", []),
                }

            results.append(result)
        except Exception as e:
            errors.append({"row": idx + 1, "error": str(e)})

    placed_count = sum(1 for r in results if r["placed"])
    avg_prob = round(sum(r["probability"] for r in results) / len(results), 2) if results else 0

    return {
        "filename": filename,
        "total_students": len(results),
        "placed_count": placed_count,
        "not_placed_count": len(results) - placed_count,
        "avg_probability": avg_prob,
        "placement_rate": round(placed_count / len(results) * 100, 1) if results else 0,
        "results": results,
        "errors": errors,
    }
