import matplotlib.pyplot as plt

def create_charts(df):
    charts = []

    numeric_cols = df.select_dtypes(include="number").columns[:3]

    for col in numeric_cols:
        fig, ax = plt.subplots()
        df[col].hist(ax=ax)
        ax.set_title(f"Distribution of {col}")
        charts.append(fig)

    return charts