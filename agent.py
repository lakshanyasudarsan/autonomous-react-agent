import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from tools import calculator, get_current_date, search_notes

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TOOLS = [
    {
        "type": "function",
        "name": "calculator",
        "description": "Perform a mathematical calculation.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A mathematical expression."
                }
            },
            "required": ["expression"]
        }
    },
    {
        "type": "function",
        "name": "get_current_date",
        "description": "Return the current date.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "type": "function",
        "name": "search_notes",
        "description": "Search local AI notes.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Topic to search for."
                }
            },
            "required": ["query"]
        }
    }
]

SYSTEM_PROMPT = """
You are an autonomous AI agent.

1. Understand the user's goal.
2. Decide whether a tool is needed.
3. Use the best tool.
4. Read the tool result.
5. Use another tool if required.
6. When enough information is available, give the final answer.

Do not invent tool results.
Keep final answers clear and concise.
"""

def execute_tool(name, arguments):

    if name == "calculator":
        return calculator(arguments["expression"])

    if name == "get_current_date":
        return get_current_date()

    if name == "search_notes":
        return search_notes(arguments["query"])

    return "Unknown tool."


def run_agent(user_input, max_steps=6):

    input_items = [
        {
            "role": "user",
            "content": user_input
        }
    ]

    for step in range(max_steps):

        print(f"\n--- Agent Step {step + 1} ---")

        response = client.responses.create(
            model="gpt-5",
            instructions=SYSTEM_PROMPT,
            input=input_items,
            tools=TOOLS
        )

        tool_calls = [
            item for item in response.output
            if item.type == "function_call"
        ]

        if not tool_calls:
            return response.output_text

        input_items.extend(response.output)

        for call in tool_calls:

            arguments = json.loads(call.arguments)

            print(f"Action: {call.name}")
            print(f"Arguments: {arguments}")

            observation = execute_tool(
                call.name,
                arguments
            )

            print(f"Observation: {observation}")

            input_items.append(
                {
                    "type": "function_call_output",
                    "call_id": call.call_id,
                    "output": str(observation)
                }
            )

    return "Agent stopped because it reached the maximum number of steps."


if __name__ == "__main__":

    print("Autonomous ReAct Agent")
    print("Type 'exit' to stop.")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        answer = run_agent(user_input)

        print("\nAgent:", answer)