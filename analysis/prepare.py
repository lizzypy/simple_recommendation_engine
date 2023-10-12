import os
import pandas as pd
from typing import List
import numpy as np
from analysis.prepare_genres import prepare_genres
from analysis.utils.cleaning import lower_case_and_strip_spaces
from analysis.utils.cleaning import combine_genres_list
from analysis.utils.extract import get_genres_list
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_input_data_path: str = f"{os.path.dirname(os.path.abspath(__file__))}/notebooks/input/all_movies.csv"

def prepare():
    # All the things
    movies_df: pd.DataFrame = pd.read_csv(movies_input_data_path)
    movies_df = prepare_genres(movies_df)

    # TODO - write out the cleaned data - maybe break up prep into two steps from here down
    print("Cleaned the dataset")
    # get the list of all genres
    all_genres = get_genres_list(movies_df)

    print("got the genres list")
    # Get the tf-idf matrix
    tf = TfidfVectorizer(vocabulary=all_genres)
    tfidf_matrix = tf.fit_transform(movies_df['genres'])

    print("tfidf-ed")
    # get the similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    cosine_df = pd.DataFrame(cosine_sim)
    cosine_first_10k = cosine_df.head(10)
    print(f"cosine data frame exists with stuff {cosine_first_10k.shape}")
    cosine_df.to_hdf('the_real_matrix.h5', key="stage", mode="w")
    cosine_first_10k.to_csv('the_matrix.csv')

    print("Finished!")

if __name__ == "__main__":
    prepare()
