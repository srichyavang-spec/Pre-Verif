from prompts.notification_prompt import NOTIFICATION_PROMPT
from services.gemini_service import generate_response


def explain(notification):

    prompt = f"""
{NOTIFICATION_PROMPT}

Notification

{notification}
"""

    return generate_response(prompt)