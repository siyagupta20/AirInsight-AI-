
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


POLLUTION_FEATURES = [
    "PM2.5",
    "PM10",
    "NO2",
    "SO2",
    "CO",
    "O3",
    "Benzene",
    "NO",
    "NOx",
    "NH3"
]


def preprocess_data(df):

    # Select available pollution features
    features = [
        col for col in POLLUTION_FEATURES
        if col in df.columns
    ]

    if len(features) < 2:
        raise ValueError(
            "At least two pollution features are required."
        )

    # Convert selected columns into numeric values
    X = df[features].copy()

    for col in features:
        X[col] = pd.to_numeric(
            X[col],
            errors="coerce"
        )

    # Replace infinite values with missing values
    X = X.replace([np.inf, -np.inf], np.nan)

    # Remove completely empty columns
    X = X.dropna(axis=1, how="all")

    if X.shape[1] < 2:
        raise ValueError(
            "Insufficient valid pollution features."
        )

    if len(X) < 2:
        raise ValueError(
            "At least two records are required."
        )

    # Handle missing values using median
    imputer = SimpleImputer(strategy="median")
    X_imputed = imputer.fit_transform(X)

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    # Return processed data and preprocessing objects
    return {
        "scaled_data": X_scaled,
        "imputed_data": X_imputed,
        "features": list(X.columns),
        "imputer": imputer,
        "scaler": scaler
    }
