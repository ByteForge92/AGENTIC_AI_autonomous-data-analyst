import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_ai_insights(df, plan, results):
    summary = df.describe(include='all').to_string()

    prompt = f"""
    You are a senior data analyst.

    Analysis Plan:
    {plan}

    Computed Results:
    {results}

    Dataset Summary:
    {summary}

    Generate:
    - 5-6 strong insights
    - explain relationships
    - highlight important patterns
    """

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"),
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content