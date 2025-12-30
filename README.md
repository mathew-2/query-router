# Query Router

A simple query router that uses LangChain + Ollama to route user questions to the correct agent based on intent.

## Agents

- **GitHubAgent** - Handles GitHub queries (pull requests, commits, repos)
- **LinearAgent** - Handles Linear queries (issues, tasks, sprints)

## Setup

### 1. Install Ollama

```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Start Ollama & Pull Model

```bash
ollama serve
ollama pull llama3.2
```

### 3. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

## Usage

```bash
python main.py
```

### Example

```
You: Show my open pull requests
→ GitHubAgent

You: What issues are assigned to me?
→ LinearAgent

You: What's the weather today?
→ "I cannot answer this question"
```

## Run Tests

```bash
python -m unittest test_router.py -v
```