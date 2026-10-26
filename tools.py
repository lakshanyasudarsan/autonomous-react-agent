from datetime import datetime


def calculator(expression: str):
    try:
        allowed = set("0123456789+-*/(). ")

        if not set(expression).issubset(allowed):
            return "Invalid mathematical expression."

        result = eval(expression, {"__builtins__": {}})
        return str(result)

    except Exception as e:
        return f"Calculator error: {e}"


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


def search_notes(query: str):
    notes = {
        "rag": (
            "RAG stands for Retrieval-Augmented Generation. "
            "It retrieves relevant information before generating an answer."
        ),
        "hybrid search": (
            "Hybrid search combines semantic vector search "
            "with keyword search such as BM25."
        ),
        "agentic rag": (
            "Agentic RAG lets an AI agent decide whether to "
            "rewrite queries, retrieve again, use tools, or answer."
        )
    }

    query = query.lower()

    for topic, text in notes.items():
        if topic in query:
            return text

    return "No matching information found."