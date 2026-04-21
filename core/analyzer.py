def analyze_data(df):
    result = {}

    result["summary"] = df.describe().to_dict()

    result["correlation"] = df.corr(numeric_only=True).to_dict()

    return result
