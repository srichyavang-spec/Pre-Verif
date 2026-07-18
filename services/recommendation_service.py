from prompts.recommendation_prompt import RECOMMENDATION_PROMPT
from services.gemini_service import generate_response


def recommend(profile):

    prompt = f"""
{RECOMMENDATION_PROMPT}

Student Details

Rank : {profile.rank}

Category : {profile.category}

Branch : {profile.branch}

State : {profile.state}
"""

    return generate_response(prompt)