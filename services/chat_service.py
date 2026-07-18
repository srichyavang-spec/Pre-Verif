from prompts.system_prompt import SYSTEM_PROMPT
from services.gemini_service import generate_response


def chat(message: str):

    prompt = f"""
{SYSTEM_PROMPT}

Student Question:

{message}
"""

    return generate_response(prompt)