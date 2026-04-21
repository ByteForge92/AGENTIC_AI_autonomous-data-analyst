def clean_data(df):
    report = {}

    missing = df.isnull().sum()
    report["missing_values"] = missing.to_dict()

    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include="object").columns:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])

    return df, report