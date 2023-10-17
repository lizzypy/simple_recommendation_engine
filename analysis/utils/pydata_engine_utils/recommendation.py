import numpy
import pandas as pd


def get_similar_movies(title: str, similarity_matrix: numpy.ndarray, movies: pd.DataFrame, movies_to_rec: int):
    titles = movies['title']
    indices = pd.Series(movies.index, index=movies['title'])

    movie_index = indices[title]
    sim_scores = list(enumerate(similarity_matrix[movie_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:movies_to_rec+1]
    movie_indices = [i[0] for i in sim_scores]
    return list(titles.iloc[movie_indices].values)
