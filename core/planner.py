import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_plan(df):
    columns = list(df.columns)

    prompt = f"""
    You are a senior data analyst.

    Given dataset columns:
    {columns}

    Create a step-by-step analysis plan.

    Include:
    - important metrics to compute
    - relationships to explore
    - trends to check

    Output as bullet points.
    """

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"),
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content