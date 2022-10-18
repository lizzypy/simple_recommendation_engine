from typing import List

import pandas as pd
import pytest
import os

from analysis.utils.cleaning import lower_case_and_strip_spaces, combine_genres_list, find_duplicates_and_combine
from analysis.utils.fixtures.movies import expected_movies_dataframe
from pandas._testing import assert_frame_equal


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DUPLICATE_MOVIE_FIXTURE_PATH = f"{BASE_PATH}/fixtures/duplicated_movie_fixture.csv"


@pytest.mark.parametrize(
    "input, expected",
    [
        (" comedy|FANTASY|Action ", "comedy|fantasy|action"),
        (" FANTASY ", "fantasy"),
        (" comedy ", "comedy"),
    ],
)
def test_lower_case_and_strip_spaces(input, expected):
    assert False


def test_combine_genres_list(genre_string_list, combined):
    assert False


