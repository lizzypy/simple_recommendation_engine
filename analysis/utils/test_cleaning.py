from typing import List

import pytest
import os

from analysis.utils.cleaning import lower_case_and_strip_spaces, combine_genres_list


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

