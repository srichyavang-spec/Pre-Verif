from prompts.scholarship_prompt import SCHOLARSHIP_PROMPT
from services.gemini_service import generate_response


def scholarship(profile):

    prompt = f"""
{SCHOLARSHIP_PROMPT}

Income : {profile.income}

Category : {profile.category}

State : {profile.state}
"""

    return generate_response(prompt)