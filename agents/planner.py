#"""Planner agent responsible for outlining the project roadmap."""

# Agent 1
from __future__ import annotations

from typing import Any, Iterable, Optional

from crewai import Agent

from config.settings import build_crewai_llm

SYSTEM_PROMPT = (
    """You are a strategic planning agent.
Your responsibility is to turn broad or unclear objectives into detailed, organized, step-by-step plans.
Your outputs must always include timelines, milestones, dependencies, and potential risks.
You should be very clear about every detail task you assign to people so there are no confusions amongst the team members."""
)


def create_planner_agent(
    tools: Optional[Iterable[object]] = None,
    llm_overrides: dict[str, Any] | None = None,
) -> Agent:
    """Create the planner agent used to bootstrap the workflow."""
    return Agent(
        name="ROADMAP INSTRUCTOR",
        role="To tell the path that is going to be followed",      #"Architect the workshop roadmap and align deliverables",
        goal="To produce a well dedicated plan that allows successful execution of any research task or reviewing.",#"Produce a milestone-driven execution plan covering research, authoring, and review",
        backstory=(
            '''A planner ai generates a plan and defines what each component of the project is gonna be able to do
              and we are equipped with skills to manage tasks based on the potential and skill of each member
            '''
        ),
        llm=build_crewai_llm(**(llm_overrides or {})),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []), ## Call tools here
    )
