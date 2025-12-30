import unittest
from unittest.mock import patch, MagicMock


class TestQueryRouter(unittest.TestCase):
    """Tests for QueryRouter."""

    @patch('router.OllamaLLM')
    def setUp(self, mock_ollama):
        """Set up test fixtures with mocked LLM."""
        self.mock_llm = MagicMock()
        mock_ollama.return_value = self.mock_llm
        
        from router import QueryRouter
        self.router = QueryRouter()

    def test_routes_to_github_agent(self):
        """Test that GitHub-related queries route to GitHubAgent."""
        self.mock_llm.invoke.return_value = "GitHubAgent"
        
        response = self.router.route("Show my open pull requests")
        self.assertIn("pull request", response.lower())

    def test_routes_to_linear_agent(self):
        """Test that Linear-related queries route to LinearAgent."""
        self.mock_llm.invoke.return_value = "LinearAgent"
        
        response = self.router.route("What issues are assigned to me?")
        self.assertIn("issue", response.lower())

    def test_unmatched_query_returns_error(self):
        """Test that unmatched queries return the error message."""
        self.mock_llm.invoke.return_value = "None"
        
        response = self.router.route("What's the weather today?")
        self.assertEqual(response, "I cannot answer this question")

    def test_empty_query_returns_error(self):
        """Test that empty queries return error message."""
        response = self.router.route("")
        self.assertEqual(response, "I cannot answer this question")


if __name__ == "__main__":
    unittest.main()
