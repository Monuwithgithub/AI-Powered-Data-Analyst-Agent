def basic_eda(df):
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
        "summary": df.describe().to_dict()
    }
def basic_eda(df):
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "summary": df.describe(include='all').to_dict()
    }