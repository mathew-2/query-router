
from .base import BaseAgent


class LinearAgent(BaseAgent):
    """Agent that handles Linear-related queries."""

    @property
    def name(self) -> str:
        return "LinearAgent"

    @property
    def description(self) -> str:
        return "Handles Linear-related queries like issues, tasks, sprints, assignments, backlogs, and project management."

    def handle(self, query: str) -> str:
        """Return mocked Linear responses."""
        return (
            "Issues assigned to you:\n"
            "  1. ENG-423 - Implement search (In Progress)\n"
            "  2. ENG-419 - Write documentation (Todo)\n"
            "  3. ENG-415 - Security review (Backlog)"
        )
