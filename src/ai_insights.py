def generate_ai_insights(df):

    insights = []

    # Dataset size
    insights.append(f"📊 Dataset has {df.shape[0]} rows and {df.shape[1]} columns.")

    # Missing values
    missing = df.isnull().sum().sum()
    insights.append(f"⚠️ Total missing values: {missing}")

    # Numeric columns
    num_cols = df.select_dtypes(include='number').columns
    insights.append(f"🔢 Numeric columns: {len(num_cols)}")

    # High variance column
    if len(num_cols) > 0:
        high_var_col = df[num_cols].var().idxmax()
        insights.append(f"📈 '{high_var_col}' has highest variation.")

    # Categorical column insight
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) > 0:
        top_cat = df[cat_cols[0]].value_counts().idxmax()
        insights.append(f"🏷️ Most frequent value in '{cat_cols[0]}' is '{top_cat}'.")

    # General insights
    insights.append("📌 Data is structured and ready for analysis.")
    insights.append("📊 Visualization can reveal important trends.")
    insights.append("🤖 ML models can be applied for prediction tasks.")

    return insights