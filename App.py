import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_ingestion import load_data
from src.eda_engine import basic_eda
from src.insight_generator import generate_insights

# Page config
st.set_page_config(page_title="AI Data Analyst", layout="wide")

# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.write("Upload and analyze your datasets")

# Title
st.title("📊 AI Data Analyst Agent")

# File uploader
uploaded_files = st.file_uploader(
    "Upload CSV files",
    type=["csv"],
    accept_multiple_files=True
)

# ✅ MAIN LOGIC
if uploaded_files:

    for uploaded_file in uploaded_files:

        # Load data
        df = load_data(uploaded_file)

        # Clean column names
        df.columns = df.columns.str.strip()

        st.markdown(f"## 📁 File: {uploaded_file.name}")
        # ✅ DASHBOARD HEADER
        st.markdown("""
              <div style="
                 padding:15px;
                 border-radius:10px;
                 background: linear-gradient(135deg, #36d1dc, #5b86e5);
                 color:white;
                 text-align:center;
                 font-size:20px;
                 font-weight:bold;">
                 📊 Smart Data Dashboard
              </div>
        """, unsafe_allow_html=True)

        # ✅ KPI CARDS
        col1, col2, col3 = st.columns(3)

        col1.metric("📊 Rows", df.shape[0])
        col2.metric("📂 Columns", df.shape[1])
        col3.metric("⚠️ Missing Values", df.isnull().sum().sum())

        # Preview
        st.subheader("📌 Data Preview")
        st.dataframe(df.head())

        # EDA
        eda_results = basic_eda(df)

        # ---------------------------
        # 📊 VISUALIZATION SECTION
        # ---------------------------
        st.subheader("📈 Visualizations")

        column = st.selectbox(
            f"Select column for {uploaded_file.name}",
            df.columns,
            key=f"col_{uploaded_file.name}"
        )

        plot_type = st.selectbox(
            f"Select plot type for {column}",
            ["Histogram", "Bar Chart", "Box Plot"],
            key=f"plot_{uploaded_file.name}"
        )

        st.write(f"📊 Showing {plot_type} for: {column}")

        fig, ax = plt.subplots()

        # Histogram (numeric only)
        if plot_type == "Histogram":
            if df[column].dtype != 'object':
                sns.histplot(df[column].dropna(), ax=ax)
                ax.set_title(f"Histogram of {column}")
                st.pyplot(fig)
            else:
                st.warning("⚠️ Histogram works only for numeric columns")

        # Bar Chart
        elif plot_type == "Bar Chart":
            sns.countplot(x=df[column], ax=ax)
            plt.xticks(rotation=45)
            ax.set_title(f"Bar Chart of {column}")
            st.pyplot(fig)

        # Box Plot (numeric only)
        elif plot_type == "Box Plot":
            if df[column].dtype != 'object':
                sns.boxplot(x=df[column], ax=ax)
                ax.set_title(f"Box Plot of {column}")
                st.pyplot(fig)
            else:
                st.warning("⚠️ Box plot works only for numeric columns")

        # ---------------------------
        # 🤖 AI INSIGHTS
        # ---------------------------
        st.subheader("🤖 AI Insights")

        insights = generate_insights(eda_results)
        st.write(insights)
        for insight in insights:
            st.markdown(f"""
            <div style="
                padding:12px;
                margin:10px 0;
                border-radius:12px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color:white;
                font-size:16px;
                font-weight:500;">
                {insight}
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        # ---------------------------
        # 🤖 ML MODEL (FINAL CLEAN)
        # ---------------------------
    from src.ml_model import train_model

    st.subheader("🤖 ML Model")

    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) == 0:
     st.warning("⚠️ No numeric columns available for ML")

    else:  
     target = st.selectbox(
        f"Select target column for {uploaded_file.name}",
        numeric_cols,
        key=f"target_{uploaded_file.name}_{df.shape[0]}"   # ✅ UNIQUE
    )

    if st.button("Train Model", key=f"train_{uploaded_file.name}_{df.shape[1]}"):

        model, feature_cols, score = train_model(df, target)

        if model:
            st.success(f"✅ Model trained! Accuracy (R²): {round(score, 2)}")
        else:
            st.error("❌ Model training failed")
 
    ## OpenAI Insights
    from src.ai_insights import generate_ai_insights

    st.subheader("🧠 AI Insights")

    if st.button("Generate AI Insights ", key=f"ai_{uploaded_file.name}"):

     ai_text = generate_ai_insights(df)

     for insight in ai_text:
           st.write(insight)
else:
 st.info("👆 Upload at least one CSV file to begin")