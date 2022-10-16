from typing import List

import pandas as pd
import pytest
import os
from fixtures.movies import expected_movies_dataframe
from pandas._testing import assert_frame_equal


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DUPLICATE_MOVIE_FIXTURE_PATH = f"{BASE_PATH}/fixtures/duplicated_movie_fixture.csv"

@pytest.mark.parametrize(
    "initial, expected",
    [
        ("Crime|drama|HORROR", "crime|drama|horror"),
        (" CRIME|DRAMA|HORROR ", "crime|drama|horror"),
        (" CRIME ", "crime"),
        (" comedy ", "comedy"),
    ],
)
def test_lower_case_and_strip_spaces(initial, expected):
    pass


def test_combine_genres_list(genre_string_list, combined):
    pass


def test_find_duplicates_and_combine(expected_movies_dataframe):
    pass


