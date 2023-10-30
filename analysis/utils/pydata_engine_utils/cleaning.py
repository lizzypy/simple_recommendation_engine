from typing import List, Set
import pandas as pd

def lower_case_and_strip_spaces(input: str) -> str:
    return input.lower().strip()


def combine_genres_list(input: List[str]) -> Set:
    all_genres = set()
    for genre_string in input:
        genres = genre_string.split('|')
        for genre in genres:
            all_genres.add(genre)
    return all_genres


def prepare_genres(movies: pd.DataFrame) -> pd.DataFrame:
    movies_cleaned_df = movies.copy()
    movies_cleaned_df['genres'] = movies_cleaned_df['genres'].apply(lower_case_and_strip_spaces)

    movies_cleaned_df = movies_cleaned_df.loc[movies_cleaned_df['genres'] != '(no genres listed)']

    # group movies by title and combine their genres list
    movies_cleaned_df = movies_cleaned_df.groupby('title').agg({'genres': lambda x: x.to_list()}).reset_index()
    movies_cleaned_df['genres'] = movies_cleaned_df['genres'].apply(combine_genres_list)

    # make genres list into a "sentence"
    movies_cleaned_df['genres'] = movies_cleaned_df['genres'].apply(lambda x: ' '.join(x))

    return movies_cleaned_df
