import os
import pandas as pd
from pydata_engine_utils import cleaning

initial_data_fixture_path: str = f"{os.path.dirname(os.path.abspath(__file__))}/fixtures/initial_data_fixture.csv"
cleaned_data_fixture_path: str = f"{os.path.dirname(os.path.abspath(__file__))}/fixtures/cleaned_data_fixture.csv"


def test_prepare_genres():
    initial_data: pd.DataFrame = pd.read_csv(initial_data_fixture_path)
    expected_data: pd.DataFrame = pd.read_csv(cleaned_data_fixture_path)

    actual_prepared_data: pd.DataFrame = cleaning.prepare_genres(initial_data)

    actual_num_of_rows = actual_prepared_data.shape[0]
    expected_num_of_rows = expected_data.shape[0]

    assert actual_num_of_rows == expected_num_of_rows

    for i in range(actual_num_of_rows):
        actual_genres = actual_prepared_data.iloc[i]["genres"]
        expected_genres = expected_data.iloc[i]["genres"]
        assert set(actual_genres.split(" ")) == set(expected_genres.split(" "))
