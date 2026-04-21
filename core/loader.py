import pandas as pd

def load_data(file):
    file.seek(0)
    return pd.read_csv(file)