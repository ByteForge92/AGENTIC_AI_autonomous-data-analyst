from core.loader import load_data
from core.cleaner import clean_data
from core.visualizer import create_charts
from core.planner import generate_plan
from core.auto_analyst import auto_analyze
from core.ai_insights import generate_ai_insights

def run_pipeline(file):
    df = load_data(file)

    df_clean, report = clean_data(df)

    plan = generate_plan(df_clean)
    results = auto_analyze(df_clean)

    charts = create_charts(df_clean)
    insights = generate_ai_insights(df_clean, plan, results)

    return df_clean, charts, plan, insights

from core.nlq import generate_query_code, execute_query

def run_query(df, query):
    code = generate_query_code(df, query)
    result = execute_query(df, code)
    return code, result