from prompts.document_prompt import DOCUMENT_PROMPT
from services.gemini_service import generate_response


def verify(document_text):

    prompt = f"""
{DOCUMENT_PROMPT}

Document

{document_text}
"""

    return generate_response(prompt)