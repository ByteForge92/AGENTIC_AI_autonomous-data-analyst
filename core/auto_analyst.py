def auto_analyze(df):
    results = {}
    
    numeric_cols = df.select_dtypes(include="number").columns

    results["means"] = df[numeric_cols].mean().to_dict()
    results["correlation"] = df[numeric_cols].corr().to_dict()

    return results