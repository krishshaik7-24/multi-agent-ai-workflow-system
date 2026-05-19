from typing import Dict, Any, List

try:
    from crewai import Agent
    CREWAI_AVAILABLE = True
except Exception:
    Agent = None
    CREWAI_AVAILABLE = False


def get_crewai_agent_profiles() -> List[Dict[str, Any]]:
    """
    Creates CrewAI-style agent profiles for the workflow.

    These profiles define the role, goal, and responsibility of each agent.
    LangGraph handles the actual workflow execution.
    """

    profiles = [
        {
            "name": "Validation Agent",
            "role": "Business Data Validator",
            "goal": "Check workflow tasks for missing, incomplete, or inconsistent information.",
            "backstory": "Specializes in reviewing business records before they move to downstream systems.",
        },
        {
            "name": "Summarization Agent",
            "role": "Business Content Summarizer",
            "goal": "Create short summaries from workflow task descriptions.",
            "backstory": "Helps teams quickly understand long task descriptions and operational updates.",
        },
        {
            "name": "Structured Output Agent",
            "role": "Structured Data Generator",
            "goal": "Convert workflow task information into clean structured output.",
            "backstory": "Prepares reliable JSON-style outputs for reporting and downstream automation.",
        },
    ]

    return profiles


def build_crewai_agents():
    """
    Builds CrewAI Agent objects when CrewAI is available.
    """

    if not CREWAI_AVAILABLE:
        return []

    crewai_agents = []

    for profile in get_crewai_agent_profiles():
        agent = Agent(
            role=profile["role"],
            goal=profile["goal"],
            backstory=profile["backstory"],
            verbose=False,
        )
        crewai_agents.append(agent)

    return crewai_agents