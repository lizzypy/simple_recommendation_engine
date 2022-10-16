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
    actual: str = lower_case_and_strip_spaces(input)
    assert actual == expected

@pytest.mark.parametrize(
    "genre_string_list, combined",
    [
        (["crime|drama|horror", "crime|drama|action"], "crime|drama|horror|action"),
        (["crime|drama|horror", "fantasy"], "crime|drama|horror|fantasy"),
        (["horror", "crime|drama|fantasy"], "horror|crime|drama|fantasy"),
        (["horror", "fantasy", "crime"], "horror|fantasy|crime"),
    ],
)
def test_combine_genres_list(genre_string_list, combined):
    actual: str = combine_genres_list(genre_string_list)
    assert actual == combined


def test_find_duplicates_and_combine(expected_movies_dataframe):
    initial_df: pd.DataFrame = pd.read_csv(DUPLICATE_MOVIE_FIXTURE_PATH)
    list_of_dup_titles: List = ['Aladdin (1992)', 'Forrest Gump (1994)']
    actual_df: pd.DataFrame = find_duplicates_and_combine(initial_df, list_of_dup_titles)
    assert_frame_equal(actual_df, expected_movies_dataframe)


