# CrewAI Demo

This repo contains a basic example for [CrewAI](https://github.com/joaomdmoura/crewai).

## Setup

1. Install dependencies:
   ```bash
   pip install crewai langchain-openai
   ```
2. Set your OpenAI API key in the environment:
   ```bash
   export OPENAI_API_KEY=<your key>
   ```

## Run the example

Execute the demo script to see two agents collaborate on a simple task:

```bash
python example.py
```

The script creates a **Researcher** agent and a **Writer** agent. The Researcher finds an AI trend, and the Writer produces a short description using that trend.
