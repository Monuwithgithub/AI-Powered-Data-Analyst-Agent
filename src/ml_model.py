from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_model(df, target_column):

    df = df.select_dtypes(include='number').dropna()

    if target_column not in df.columns:
        return None, None, "Target must be numeric"

    X = df.drop(columns=[target_column])
    y = df[target_column]

    if X.shape[1] == 0:
        return None, None, "No features available"

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    return model, X.columns, score