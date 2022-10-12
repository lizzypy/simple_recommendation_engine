from typing import List

import pandas as pd
import pytest
import os
from pandas._testing import assert_frame_equal

from analysis.utils.cleaning import lower_case_and_strip_spaces, combine_genres_list, find_duplicates_and_combine

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DUPLICATE_MOVIE_FIXTURE_PATH = f"{BASE_PATH}/fixtures/duplicated_movie_fixture.csv"

def test_lower_case_and_strip_scenario_1():
    initial: str = "Crime|drama|HORROR"
    expected: str = "crime|drama|horror"

    actual = lower_case_and_strip_spaces(initial)
    assert actual == expected


def test_lower_case_and_strip_scenario_2():
    initial_2: str = " CRIME|DRAMA|HORROR "
    expected_2: str = "crime|drama|horror"

    actual = lower_case_and_strip_spaces(initial_2)
    assert actual == expected_2


def test_lower_case_and_strip_scenario_3():
    initial_3: str = " CRIME "
    expected_3: str = "crime"

    actual = lower_case_and_strip_spaces(initial_3)
    assert actual == expected_3


def test_lower_case_and_strip_scenario_4():
    initial_4: str = " comedy "
    expected_4: str = "comedy"
    actual = lower_case_and_strip_spaces(initial_4)
    assert actual == expected_4


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
    actual = lower_case_and_strip_spaces(initial)
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


def test_find_duplicates_and_combine():
    initial_df: pd.DataFrame = pd.read_csv(DUPLICATE_MOVIE_FIXTURE_PATH)
    list_of_dup_titles: List = ['Aladdin (1992)', 'Forrest Gump (1994)']
    actual_movies_dataframe: pd.DataFrame = find_duplicates_and_combine(initial_df, list_of_dup_titles)
    assert_frame_equal(_expected_movies_dataframe().reset_index(drop=True),
                       actual_movies_dataframe.reset_index(drop=True))


# TODO put this in a fixture as well
def _expected_movies_dataframe():
    data = [[588, "Aladdin (1992)", "adventure|animation|children|comedy|musical|fantasy"],
            [114240, "Aladdin (1992)", "adventure|animation|children|comedy|musical|fantasy"],
            [356, "Forrest Gump (1994)", "comedy|drama|romance|war|action"],
            [1236, "Forrest Gump (1994)", "comedy|drama|romance|war|action"],
            [1, "Toy Story (1995)", "adventure|animation|children|comedy|fantasy"]]
    return pd.DataFrame(data, columns=['movieId', 'title', 'genres'])


