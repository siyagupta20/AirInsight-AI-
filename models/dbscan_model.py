
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA


def run_dbscan(df, eps=0.8, min_samples=5):

    features = [
        "PM2.5", "PM10", "NO2", "SO2", "CO",
        "O3", "Benzene", "NO", "NOx", "NH3"
    ]

    features = [col for col in features if col in df.columns]

    if len(features) < 2:
        raise ValueError("Not enough pollution features for DBSCAN.")

    X = df[features].copy()

    for col in features:
        X[col] = pd.to_numeric(X[col], errors="coerce")

    X = X.replace([np.inf, -np.inf], np.nan)
    X = X.dropna(axis=1, how="all")

    if X.shape[1] < 2:
        raise ValueError("Insufficient valid pollution features.")

    if len(X) < 2:
        raise ValueError("At least two records are required.")

    if eps <= 0 or min_samples < 1:
        raise ValueError("eps must be positive and min_samples must be at least 1.")

    imputer = SimpleImputer(strategy="median")
    X_imputed = imputer.fit_transform(X)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    model = DBSCAN(
        eps=eps,
        min_samples=min_samples
    )

    labels = model.fit_predict(X_scaled)

    result = df.copy()
    result["Cluster"] = labels

    noise_count = int(np.sum(labels == -1))

    analysis_data = pd.DataFrame(
        X_imputed,
        columns=X.columns,
        index=df.index
    )

    analysis_data["Cluster"] = labels

    cluster_data = analysis_data[
        analysis_data["Cluster"] != -1
    ]

    cluster_summary = (
        cluster_data["Cluster"]
        .value_counts()
        .sort_index()
        .to_dict()
    )

    cluster_profiles = (
        cluster_data.groupby("Cluster")[list(X.columns)]
        .mean()
        .round(2)
        .to_dict(orient="index")
    )

    cluster_summary = {
        int(k): int(v)
        for k, v in cluster_summary.items()
    }

    cluster_profiles = {
        int(k): {
            col: float(value)
            for col, value in profile.items()
        }
        for k, profile in cluster_profiles.items()
    }

    cluster_count = len(set(labels) - {-1})

    pca = PCA(n_components=2)
    coordinates = pca.fit_transform(X_scaled)

    result["PCA1"] = coordinates[:, 0]
    result["PCA2"] = coordinates[:, 1]

    return {
    "data": df,
    "cluster_count": cluster_count,
    "noise_count": noise_count,
    "cluster_summary": cluster_summary,
    "cluster_profiles": cluster_profiles,
    "labels": labels.tolist(),
    "features": features,
    "pca": coordinates.tolist(),
    "scaled_data": X_scaled.tolist()
}