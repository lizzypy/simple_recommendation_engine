from typing import List, Set

import pandas as pd


def lower_case_and_strip_spaces(input: str) -> str:
    return input.lower().strip()


def combine_genres_list(input: List[str]) -> str:
    all_genres: List[str] = []
    for genre_str in input:
        genre_list: List = genre_str.split('|')
        for genre in genre_list:
            if genre not in all_genres:
                all_genres.append(genre)
    return '|'.join(all_genres)


def find_duplicates_and_combine(initial_df: pd.DataFrame, duplicate_titles: List[str]) -> pd.DataFrame:
    for title in duplicate_titles:
        rows_with_genres_to_combine = initial_df.loc[initial_df['title'] == title]
        all_genres: List = []
        for idx, row in rows_with_genres_to_combine.iterrows():
            genres: str = row['genres']
            all_genres.append(genres)

        all_genres_for_title: str = combine_genres_list(all_genres)

        for idx, row in rows_with_genres_to_combine.iterrows():
            rows_with_genres_to_combine.at[idx, 'genres'] = all_genres_for_title
        initial_df.loc[rows_with_genres_to_combine.index, :] = rows_with_genres_to_combine[:]
    return initial_df
