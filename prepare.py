import boto3
import pandas as pd
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def lower_case_and_strip_spaces(input: str) -> str:
    return input.lower().strip()


def combine_genres_list(input: List[str]):
    all_genres = set()
    for genre_strings in input:
        genres: List[str] = genre_strings.split('|')
        for genre in genres:
            all_genres.add(genre)
    return all_genres

def get_genres_list(movies: pd.DataFrame):
    for_genres_list_df = movies.copy()
    for_genres_list_df = for_genres_list_df['genres'].explode().reset_index()
    return list(for_genres_list_df.genres.unique())

def prepare():
    # All the things
    s3 = boto3.client('s3')

    s3.download_file('pydatapipelinebucket', 'all_movies.csv', 'local_file.csv')
    movies_df: pd.DataFrame = pd.read_csv('local_file.csv')
    movies_cleaned_df = movies_df.copy()
    movies_cleaned_df['genres'] = movies_cleaned_df['genres'].apply(lower_case_and_strip_spaces)

    movies_cleaned_df = movies_cleaned_df.loc[movies_cleaned_df['genres'] != '(no genres listed)']

    # group movies by title and combine their genres list
    movies_cleaned_df = movies_cleaned_df.groupby('title').agg({'genres': lambda x: x.to_list()}).reset_index()
    movies_cleaned_df['genres'] = movies_cleaned_df['genres'].apply(combine_genres_list)

    # make genres list into a "sentence"
    movies_cleaned_df['genres'] = movies_cleaned_df['genres'].apply(lambda x: ' '.join(x))

    movies_cleaned_df = movies_cleaned_df.head(30000)
    # movies_df = prepare_genres(movies_df)

    # TODO - write out the cleaned data - maybe break up prep into two steps from here down
    print("Got the dataset")
    # get the list of all genres
    all_genres = get_genres_list(movies_cleaned_df)

    print("got the genres list")
    # Get the tf-idf matrix
    tf = TfidfVectorizer(vocabulary=all_genres)
    tfidf_matrix = tf.fit_transform(movies_cleaned_df['genres'])

    print("tfidf-ed")
    # get the similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    cosine_df = pd.DataFrame(cosine_sim)
    cosine_first_10k = cosine_df
    print(f"cosine data frame exists with stuff {cosine_first_10k.shape}")
    cosine_first_10k.to_csv('the_matrix.csv')
    s3.upload_file('the_matrix.csv', 'pydatapipelinebucket', 'the_s3_matrix.csv')

    print("Finished!")

if __name__ == "__main__":
    prepare()

