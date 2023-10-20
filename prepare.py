import boto3
import pandas as pd
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

    # get the list of all genres
    for_genres_list_df = movies.copy()
    for_genres_list_df = movies_df['genres'].explode().reset_index()
    all_genres = list(for_genres_list_df.genres.unique())

    # Get the tf-idf matrix
    tf = TfidfVectorizer(vocabulary=all_genres)
    tfidf_matrix = tf.fit_transform(movies_cleaned_df['genres'])

    # get the similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    cosine_df = pd.DataFrame(cosine_sim)
    cosine_first_10k.to_csv('the_matrix.csv')
    s3.upload_file('the_matrix.csv', 'pydatapipelinebucket', 'the_s3_matrix.csv')

    print("Finished!")

if __name__ == "__main__":
    prepare()

