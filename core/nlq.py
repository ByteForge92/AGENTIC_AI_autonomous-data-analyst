import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_query_code(df, user_query):
    sample = df.head(10).to_csv(index=False)


    prompt = f"""
    You are a data analyst.

    Convert the user query into pandas code.

    STRICT RULES:
    - Use ONLY the existing dataframe named df
    - DO NOT create a new dataframe
    - DO NOT import anything
    - DO NOT redefine df
    - ONLY use df.columns that exist
    - ONLY return valid Python code
    - NO markdown (no ``` blocks)
    - Store final output in variable named result
    - DO NOT print anything

    If query is not related to dataset:
        result = "Query not related to dataset"

    Dataset columns:
    {list(df.columns)}

    Dataset sample:
    {sample}

    User query:
    {user_query}
    """

    response = response = client.chat.completions.create(
    model=os.getenv("GROQ_MODEL"),
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content


def execute_query(df, code):
    try:
        code = code.replace("```python", "").replace("```", "").strip()

        forbidden = ["import", "pd.", "DataFrame", "read_", "=" + " pd"]
        for word in forbidden:
            if word in code:
                return "Error: Unsafe or invalid code generated"

        local_vars = {"df": df}
        exec(code, {}, local_vars)

        return local_vars.get("result", "No result returned")

    except Exception as e:
        return f"Error: {str(e)}"

