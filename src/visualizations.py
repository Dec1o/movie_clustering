import matplotlib.pyplot as plt

def plot_kmeans_clusters(df):
    """Plota os clusters gerados pelo K-Means."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Filmes por Mês'], df['Avaliação Média'], c=df['KMeans Cluster'], cmap='viridis')
    plt.title('Clusters gerados pelo K-Means')
    plt.xlabel('Número de Filmes Assistidos por Mês')
    plt.ylabel('Avaliação Média')
    plt.colorbar(label='Cluster')
    plt.show()

def plot_dbscan_clusters(df):
    """Plota os clusters gerados pelo DBSCAN."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Filmes por Mês'], df['Avaliação Média'], c=df['DBSCAN Cluster'], cmap='plasma')
    plt.title('Clusters gerados pelo DBSCAN')
    plt.xlabel('Número de Filmes Assistidos por Mês')
    plt.ylabel('Avaliação Média')
    plt.colorbar(label='Cluster')
    plt.show()
