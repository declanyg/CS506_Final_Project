# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from scripts.config import DEFAULT_SYMBOL

def train_linear_model(input_file=None, model_file=None):
    """Train and save a linear regression model."""
    # Set default file paths if not provided
    if input_file is None:
        input_file = f"./data/processed/{DEFAULT_SYMBOL}_features.csv"
    if model_file is None:
        model_file = f"./models/{DEFAULT_SYMBOL}_linear_model.pkl"

    df = pd.read_csv(input_file)
    X = df[['Daily_Returns', 'MA_20']].fillna(0)
    y = df['Close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, model_file)
    return model

if __name__ == "__main__":
    train_linear_model()
