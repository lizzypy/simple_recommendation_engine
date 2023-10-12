import pandas as pd
from typing import List
from analysis.utils.cleaning import lower_case_and_strip_spaces
from analysis.utils.cleaning import combine_genres_list

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
