from typing import List
import pytest

from utils.transform import one_hot_encode_genres

all_genres_list: List = ['genre1', 'genre2', 'genre3', 'genre4']

@pytest.mark.parametrize(
    "genres_list, expected_encoding",
    [
        (['genre2', 'genre3'], [0, 1, 1, 0]),
        (['genre1', 'genre4'], [1, 0, 0, 1]),
        (['genre2'], [0, 1, 0, 0]),
        (['genre1', 'genre2', 'genre3', 'genre4'], [1, 1, 1, 1]),
    ],
)
def test_one_hot_encode_genres(genres_list, expected_encoding):
    actual_encoding = one_hot_encode_genres(all_genres_list, genres_list)
    assert expected_encoding == actual_encoding
