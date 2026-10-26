# Autonomous ReAct AI Agent

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

## Project Structure

```text
autonomous-react-agent/
├── agent.py
├── tools.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
