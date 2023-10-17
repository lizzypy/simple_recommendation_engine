import pytest
import os

from pydata_engine_utils.cleaning import lower_case_and_strip_spaces, combine_genres_list
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
        (["crime|drama|horror", "crime|drama|action"], {"crime", "drama", "horror", "action"}),
        (["crime|drama|horror", "fantasy"], {"crime", "drama", "horror", "fantasy"}),
        (["horror", "fantasy", "crime"], {"horror", "fantasy", "crime"}),
    ],
)
def test_combine_genres_list(genre_string_list, combined):
    actual = combine_genres_list(genre_string_list)
    assert actual == combined