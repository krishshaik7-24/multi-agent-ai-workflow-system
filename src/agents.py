from typing import Dict, Any


def validation_agent(task: Dict[str, Any]) -> Dict[str, Any]:
    """Agent 1: validates task content and checks missing business details."""
    text = str(task.get("input_text", "")).lower()

    issues = []

    if "missing" in text:
        issues.append("Input mentions missing information.")

    if len(text.strip()) < 20:
        issues.append("Input text is too short for reliable processing.")

    return {
        "agent": "Validation Agent",
        "status": "passed" if not issues else "needs_review",
        "issues": issues,
    }


def summarization_agent(task: Dict[str, Any]) -> Dict[str, Any]:
    """Agent 2: creates a short business summary."""
    text = str(task.get("input_text", ""))

    summary = text[:120]
    if len(text) > 120:
        summary += "..."

    return {
        "agent": "Summarization Agent",
        "summary": summary,
    }


def structured_output_agent(task: Dict[str, Any]) -> Dict[str, Any]:
    """Agent 3: converts task data into structured output."""
    return {
        "agent": "Structured Output Agent",
        "structured_output": {
            "task_id": task.get("task_id"),
            "department": task.get("department"),
            "task_type": task.get("task_type"),
            "priority": task.get("priority"),
            "business_action": "Review and process task based on priority.",
        },
    }