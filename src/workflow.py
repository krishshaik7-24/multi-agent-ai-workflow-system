import asyncio
from typing import Any, Dict, List, TypedDict

from langgraph.graph import END, StateGraph

from src.agents import (
    structured_output_agent,
    summarization_agent,
    validation_agent,
)
from src.utils import validate_required_fields


class WorkflowState(TypedDict):
    task: Dict[str, Any]
    results: Dict[str, Any]


async def validate_node(state: WorkflowState) -> WorkflowState:
    task = state["task"]

    field_check = validate_required_fields(task)
    agent_result = validation_agent(task)

    state["results"]["field_validation"] = field_check
    state["results"]["content_validation"] = agent_result

    await asyncio.sleep(0.1)
    return state


async def summarize_node(state: WorkflowState) -> WorkflowState:
    task = state["task"]

    summary_result = summarization_agent(task)
    state["results"]["summary"] = summary_result

    await asyncio.sleep(0.1)
    return state


async def structure_node(state: WorkflowState) -> WorkflowState:
    task = state["task"]

    structured_result = structured_output_agent(task)
    state["results"]["structured_output"] = structured_result

    await asyncio.sleep(0.1)
    return state


def build_workflow():
    workflow = StateGraph(WorkflowState)

    workflow.add_node("validate", validate_node)
    workflow.add_node("summarize", summarize_node)
    workflow.add_node("structure", structure_node)

    workflow.set_entry_point("validate")
    workflow.add_edge("validate", "summarize")
    workflow.add_edge("summarize", "structure")
    workflow.add_edge("structure", END)

    return workflow.compile()


async def run_single_task(task: Dict[str, Any]) -> Dict[str, Any]:
    app = build_workflow()

    initial_state: WorkflowState = {
        "task": task,
        "results": {},
    }

    final_state = await app.ainvoke(initial_state)

    return {
        "task_id": task.get("task_id"),
        "department": task.get("department"),
        "task_type": task.get("task_type"),
        "priority": task.get("priority"),
        "workflow_results": final_state["results"],
    }


async def run_all_tasks(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    async_jobs = [run_single_task(task) for task in tasks]
    return await asyncio.gather(*async_jobs)