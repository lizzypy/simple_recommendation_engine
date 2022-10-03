from typing import List, Set

import pandas as pd


def lower_case_and_strip_spaces(input: str):
    return input.lower().strip()


def combine_genres_list(genres_strings: List[str]):
    all_genres: List = []

    for genre_string in genres_strings:
        genres: List = genre_string.split('|')
        for genre in genres:
            if genre not in all_genres:
                all_genres.append(genre)

    return '|'.join(all_genres)


def find_duplicates_and_combine(all_data: pd.DataFrame, list_of_duplicate_titles: List[str]):
    for title in list_of_duplicate_titles:
        rows_with_genres_to_combine = all_data.loc[all_data['title'] == title]
        all_genres: List = []
        for idx, row in rows_with_genres_to_combine.iterrows():
            genres: str = row['genres']
            all_genres.append(genres)

        all_genres_for_title: str = combine_genres_list(all_genres)

        for idx, row in rows_with_genres_to_combine.iterrows():
            rows_with_genres_to_combine.at[idx, 'genres'] = all_genres_for_title
        all_data.loc[rows_with_genres_to_combine.index, :] = rows_with_genres_to_combine[:]
    return all_data
