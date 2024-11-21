import numpy as np
import pandas as pd
import sys
import os

def generate_movie_data(n=100):
    """Gera um dataset sintético para hábitos de assistir filmes."""
    np.random.seed(42)
    
    # Número de filmes assistidos por mês
    n_filmes = np.random.randint(1, 30, size=n)

    # Gênero preferido (1: Ação, 2: Comédia, 3: Drama, 4: Terror, 5: Romance)
    genero_preferido = np.random.randint(1, 6, size=n)

    # Frequência de ida ao cinema (dias por mês)
    frequencia_cinema = np.random.randint(0, 8, size=n)

    # Avaliação média dos filmes (1 a 10)
    avaliacao_media = np.random.randint(1, 11, size=n)

    # Criando o DataFrame
    df = pd.DataFrame({
        'Filmes por Mês': n_filmes,
        'Gênero Preferido': genero_preferido,
        'Ida ao Cinema (dias/mês)': frequencia_cinema,
        'Avaliação Média': avaliacao_media
    })
    
    return df

# Gerar e salvar o dataset
if __name__ == "__main__":
    df = generate_movie_data()
    df.to_csv('data/dataset.csv', index=False)
    print("Dataset gerado e salvo em 'data/dataset.csv'")
