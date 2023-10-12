import pandas as pd

def get_genres_list(movies: pd.DataFrame):
    for_genres_list_df = movies.copy()
    for_genres_list_df = for_genres_list_df['genres'].explode().reset_index()
    return list(for_genres_list_df.genres.unique())
