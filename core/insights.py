def generate_insights(df):
    insights = []

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        mean = df[col].mean()
        max_val = df[col].max()
        min_val = df[col].min()

        insights.append(
            f"{col}: average is {mean:.2f}, highest is {max_val:.2f}, lowest is {min_val:.2f}"
        )

    return insights