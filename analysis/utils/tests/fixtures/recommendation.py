import pytest
from numpy import array


@pytest.fixture
def _get_similarity_martix():
    return array([[1, 0.6, 0.8, 0.7, 0.5],
                  [0.6, 1, 0.5, 0.9, 0.4],
                  [0.8, 0.5, 1, 0.3, 0.6],
                  [0.7, 0.9, 0.3, 1, 0.2],
                  [0.5, 0.4, 0.6, 0.2, 1]])