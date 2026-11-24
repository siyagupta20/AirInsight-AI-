import numpy as np
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)


def evaluate_clustering(X, labels):

    X = np.asarray(X)
    labels = np.asarray(labels)

    valid_mask = labels != -1

    X_valid = X[valid_mask]
    labels_valid = labels[valid_mask]

    unique_clusters = np.unique(labels_valid)
    n_clusters = len(unique_clusters)

    if n_clusters < 2:
        return {
            "silhouette_score": None,
            "davies_bouldin_score": None,
            "calinski_harabasz_score": None,
            "clusters_evaluated": n_clusters,
            "records_evaluated": len(X_valid),
            "message": "At least 2 clusters are required for evaluation."
        }

    if len(X_valid) <= n_clusters:
        return {
            "silhouette_score": None,
            "davies_bouldin_score": None,
            "calinski_harabasz_score": None,
            "clusters_evaluated": n_clusters,
            "records_evaluated": len(X_valid),
            "message": "Not enough records to calculate evaluation metrics."
        }

    try:
        silhouette = silhouette_score(X_valid, labels_valid)
        davies_bouldin = davies_bouldin_score(X_valid, labels_valid)
        calinski_harabasz = calinski_harabasz_score(X_valid, labels_valid)

        return {
            "silhouette_score": round(float(silhouette), 4),
            "davies_bouldin_score": round(float(davies_bouldin), 4),
            "calinski_harabasz_score": round(float(calinski_harabasz), 4),
            "clusters_evaluated": n_clusters,
            "records_evaluated": len(X_valid),
            "message": "Evaluation completed successfully."
        }

    except Exception as e:
        return {
            "silhouette_score": None,
            "davies_bouldin_score": None,
            "calinski_harabasz_score": None,
            "clusters_evaluated": n_clusters,
            "records_evaluated": len(X_valid),
            "message": str(e)
        }