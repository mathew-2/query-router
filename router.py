"""Query router using LangChain with Ollama for intent classification."""

import os
import logging
from typing import Optional

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

from agents import BaseAgent, GitHubAgent, LinearAgent

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class QueryRouter:
    """Routes queries to the appropriate agent using LLM-based intent classification."""

    CLASSIFICATION_PROMPT = PromptTemplate(
        input_variables=["agents_info", "query"],
        template="""You are a query classifier. Your job is to determine which agent should handle a user query.

Available agents:
{agents_info}

User query: "{query}"

Respond with ONLY the agent name (e.g., "GitHubAgent" or "LinearAgent").
If no agent is appropriate, respond with "None".

Agent:"""
    )

    def __init__(self):
        """Initialize the router with Ollama LLM and agents."""
        # Get configuration from environment
        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        model_name = os.getenv("OLLAMA_MODEL", "llama3.2")

        # Initialize Ollama LLM
        self.llm = OllamaLLM(
            base_url=ollama_base_url,
            model=model_name,
            temperature=0  # Deterministic output for classification
        )

        # Register agents
        self._agents: dict[str, BaseAgent] = {}
        self._register_agent(GitHubAgent())
        self._register_agent(LinearAgent())

        logger.info(f"Router initialized with model: {model_name}")

    def _register_agent(self, agent: BaseAgent) -> None:
        """Register an agent with the router."""
        self._agents[agent.name] = agent
        logger.info(f"Registered agent: {agent.name}")

    def register_agent(self, agent: BaseAgent) -> None:
        """Public method to register new agents (for extensibility)."""
        self._register_agent(agent)

    def _get_agents_info(self) -> str:
        """Generate a description of all available agents."""
        return "\n".join(
            f"- {agent.name}: {agent.description}"
            for agent in self._agents.values()
        )

    def _classify_intent(self, query: str) -> Optional[str]:
        """Use LLM to classify the query intent and return agent name."""
        prompt = self.CLASSIFICATION_PROMPT.format(
            agents_info=self._get_agents_info(),
            query=query
        )

        try:
            response = self.llm.invoke(prompt).strip()
            # Clean up response - extract just the agent name
            response = response.split("\n")[0].strip()
            
            if response in self._agents:
                return response
            elif response.lower() == "none":
                return None
            else:
                # Try to find a partial match
                for agent_name in self._agents:
                    if agent_name.lower() in response.lower():
                        return agent_name
                return None
        except Exception as e:
            logger.error(f"LLM classification error: {e}")
            return None

    def route(self, query: str) -> str:
        """Route a query to the appropriate agent and return the response."""
        if not query or not query.strip():
            return "I cannot answer this question"

        agent_name = self._classify_intent(query)

        if agent_name and agent_name in self._agents:
            agent = self._agents[agent_name]
            logger.info(f"Routed to {agent.name}: '{query}'")
            return agent.handle(query)

        logger.info(f"No agent matched: '{query}'")
        return "I cannot answer this question"