from typing import List

import pytest
import os

from analysis.utils.cleaning import lower_case_and_strip_spaces, combine_genres_list
from analysis.utils.fixtures.movies import expected_movies_dataframe


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
    actual = lower_case_and_strip_spaces(input)
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
    actual = combine_genres_list(genre_string_list)
    assert actual == combined


