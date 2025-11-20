# """Researcher agent that gathers information and produces well-structured findings."""

from __future__ import annotations

from typing import Any, Iterable, Optional

from crewai import Agent

from config.settings import build_crewai_llm

SYSTEM_PROMPT = (
    "You are a dedicated Researcher Agent. "
    "Your task is to thoroughly investigate queries, explore reliable sources, "
    "analyze information, and produce clear, structured, and well-reasoned research outputs. "
    "Always aim for accuracy, depth, and clarity. "
    "Break down complex topics, compare perspectives, and ensure findings are easy to understand. "
    "If information is missing, ambiguous, or contradictory, highlight it explicitly."
)


def create_researcher_agent(
    tools: Optional[Iterable[object]] = None,
    llm_overrides: dict[str, Any] | None = None,
) -> Agent:
    """Create the researcher agent that gathers information and produces insights."""
    return Agent(
        name="Researcher Agent",
        role=(
            "Conduct deep research on assigned topics, analyze information, "
            "and produce comprehensive, structured, and clear insights."
        ),
        goal=(
            "Deliver accurate, well-explained, and insight-rich research outputs. "
            "Identify key points, trends, issues, and relevant context. "
            "Ensure each response is complete, factual, and logically organized."
        ),
        backstory=(
            "You have years of experience conducting analytical research across a wide range "
            "of domains. You excel at gathering information, synthesizing it, and transforming "
            "it into clear and accessible explanations. Your strength lies in your ability to "
            "identify important details, connect concepts, and simplify complexity without "
            "losing meaning."
        ),
        llm=build_crewai_llm(**(llm_overrides or {})),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )


# #"""Reviewer agent that checks quality, accuracy, and completeness."""

# # Agent 4
# from __future__ import annotations

# from typing import Any, Iterable, Optional

# from crewai import Agent

# from config.settings import build_crewai_llm

# SYSTEM_PROMPT = (
#     """Add system prompt content here."""
#     # "You are the Quality Reviewer for the workshop. "
#     # "Audit drafts for factual accuracy, pedagogy, deployment readiness, and alignment with the plan. "
#     # "Provide actionable feedback and highlight risks or missing pieces."
# )


# def create_reviewer_agent(
#     tools: Optional[Iterable[object]] = None,
#     llm_overrides: dict[str, Any] | None = None,
# ) -> Agent:
#     """Create the reviewer agent that validates deliverables before release."""
#     return Agent(
#         name="---",  # e.g., "Quality Reviewer"
#         role="",  # "Ensure every deliverable is accurate, actionable, and polished"
#         goal="",  # "Deliver constructive critiques and sign-off criteria before publication"
#         backstory=(
#             "If any add a backstory here."
#             # "Placeholder: Replace with scenario-specific review standards during the workshop. "
#             # "You safeguard against gaps, errors, and unclear guidance."
#         ),
#         llm=build_crewai_llm(**(llm_overrides or {})),
#         allow_delegation=False,
#         verbose=True,
#         system_prompt=SYSTEM_PROMPT,
#         tools=list(tools or []),  # Call tools here
#     )
