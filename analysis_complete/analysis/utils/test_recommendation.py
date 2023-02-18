import os
from typing import List

import numpy
import pandas as pd
import pytest
from numpy import array, genfromtxt

from analysis_complete.analysis.utils.recommendation import get_similar_movies

similarity_matrix_fixture_path: str = f"{os.path.dirname(os.path.abspath(__file__))}/fixtures/similarity_matrix_fixture.csv"
movies_fixture_path: str = f"{os.path.dirname(os.path.abspath(__file__))}/fixtures/movies_fixture.csv"


@pytest.mark.parametrize(
    "movie_title, expected_similar_movies",
    [
        ('Title 1', ['Title 3', 'Title 4']),
        ('Title 2', ['Title 4', 'Title 1']),
    ],
)
def test_get_recommendations(movie_title, expected_similar_movies):
    similartiy_matrix: numpy.ndarray = genfromtxt(similarity_matrix_fixture_path, delimiter=',')
    movies: pd.DataFrame = pd.read_csv(movies_fixture_path)

    actual_similar_movies: List = get_similar_movies(movie_title, similartiy_matrix, movies, 2)

    assert actual_similar_movies == expected_similar_movies

