import matplotlib.pyplot as plt

def plot_histogram(df, column):
    plt.figure()
    df[column].dropna().hist(bins=20)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    return plt

def plot_bar(df, column):
    plt.figure()
    df[column].value_counts().head(10).plot(kind='bar')
    plt.title(f"Top categories in {column}")
    plt.xticks(rotation=45)
    return plt