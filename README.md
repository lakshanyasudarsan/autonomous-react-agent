# Autonomous ReAct AI Agent (OpenAI)

## Overview

This project demonstrates an autonomous AI agent built from scratch in Python using a ReAct-style reasoning and tool-use loop.

The agent can decide when to use tools, execute those tools, process the observations, and continue until it produces a final answer.

## Features

- ReAct-style agent workflow
- Dynamic tool selection
- Multi-step tool use
- Calculator tool
- Date tool
- Local note search tool
- OpenAI Responses API integration
- Maximum-step safety limit

## Tech Stack

- Python
- OpenAI API
- python-dotenv

## Agent Flow

User Query  
→ Agent evaluates task  
→ Selects tool if needed  
→ Tool executes  
→ Observation returned  
→ Agent evaluates again  
→ Final answer

## Tools

- Calculator
- Current date lookup
- Local AI notes search

## Environment Setup

This project uses environment variables to keep API keys private.

### 1. Create a `.env` file

In the project root, create a file named:

```text
.env
```

Add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

### 2. Create a `.gitignore` file

If `.gitignore` is not visible in the downloaded ZIP, create it manually in the project root.

Add:

```text
.env
__pycache__/
```


### 3. Install dependencies

Run:

```bash
pip install -r requirements.txt
```

### 4. Run the agent

Run:

```bash
python agent.py
```

An OpenAI API key with available API credits is required for live model requests.

## Project Structure

```text
autonomous-react-agent/
├── agent.py
├── tools.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```
