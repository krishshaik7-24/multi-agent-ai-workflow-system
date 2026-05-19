import json
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


def load_tasks(file_path: str) -> List[Dict[str, Any]]:
    """Load workflow tasks from a CSV file."""
    data = pd.read_csv(file_path)
    return data.to_dict(orient="records")


def save_json(data: List[Dict[str, Any]], output_path: str) -> None:
    """Save workflow results as a JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def validate_required_fields(task: Dict[str, Any]) -> Dict[str, Any]:
    """Check if important task fields are available."""
    required_fields = ["task_id", "department", "task_type", "input_text", "priority"]
    missing_fields = []

    for field in required_fields:
        value = task.get(field)
        if value is None or str(value).strip() == "":
            missing_fields.append(field)

    return {
        "is_valid": len(missing_fields) == 0,
        "missing_fields": missing_fields,
    }