"""Base agent interface."""

from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Abstract base class for all agents."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the agent's name."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Return a description of what this agent handles."""
        pass

    @abstractmethod
    def handle(self, query: str) -> str:
        """Handle a query and return a response."""
        pass