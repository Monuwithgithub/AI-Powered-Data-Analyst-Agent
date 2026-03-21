def generate_insights(eda_results):
    insights = []

    # 1️⃣ Dataset size
    rows, cols = eda_results.get("shape", (0, 0))
    insights.append(f"📊 Dataset contains {rows} rows and {cols} columns.")

    # 2️⃣ Missing values analysis
    missing = eda_results.get("missing_values", {})
    total_missing = sum(missing.values())

    if total_missing > 0:
        insights.append(f"⚠️ There are {total_missing} missing values in the dataset.")
        
        high_missing_cols = [col for col, val in missing.items() if val > 0]
        if high_missing_cols:
            insights.append(f"🧩 Columns with missing values: {', '.join(high_missing_cols[:3])}")
    else:
        insights.append("✅ No missing values found — dataset is clean.")

    # 3️⃣ Feature richness
    columns = eda_results.get("columns", [])
    insights.append(f"🧠 Dataset has {len(columns)} features for analysis.")

    # 4️⃣ Numerical summary insight
    describe = eda_results.get("describe", {})
    if describe is not None and hasattr(describe, "columns"):
        insights.append("📈 Numerical features show varied distributions (check histograms for skewness).")

    # 5️⃣ Data imbalance hint
    if len(columns) > 0:
        insights.append("⚖️ Some categorical columns may have imbalance (use bar charts to verify).")

    # 6️⃣ Outlier detection hint
    insights.append("📦 Box plots may reveal outliers in numerical columns.")





    return insights