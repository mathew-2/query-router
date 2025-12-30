from .base import BaseAgent


class GitHubAgent(BaseAgent):
    """Agent that handles GitHub-related queries."""

    @property
    def name(self) -> str:
        return "GitHubAgent"

    @property
    def description(self) -> str:
        return "Handles GitHub-related queries like pull requests, commits, branches, repositories, merges, and code reviews."

    def handle(self, query: str) -> str:
        """Return mocked GitHub responses."""
        return (
            "Found 3 open pull requests:\n"
            "  1. #142 - Fix login bug\n"
            "  2. #138 - Add user settings\n"
            "  3. #135 - Update dependencies"
        )
