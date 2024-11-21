from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd

def apply_kmeans(df, n_clusters=3):
    """Aplica o algoritmo K-Means ao dataset e retorna os clusters."""
    scaler = StandardScaler()
    df_normalizado = scaler.fit_transform(df)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['KMeans Cluster'] = kmeans.fit_predict(df_normalizado)

    return df

def apply_dbscan(df, eps=0.5, min_samples=5):
    """Aplica o algoritmo DBSCAN ao dataset e retorna os clusters."""
    scaler = StandardScaler()
    df_normalizado = scaler.fit_transform(df)

    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    df['DBSCAN Cluster'] = dbscan.fit_predict(df_normalizado)

    return df
