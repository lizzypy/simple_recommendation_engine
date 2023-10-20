import boto3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pydata_engine_utils import cleaning,extract

def prepare():
    s3 = boto3.client('s3')

    s3.download_file('pydatapipelinebucket', 'all_movies.csv', 'local_file.csv')
    movies_df: pd.DataFrame = pd.read_csv('local_file.csv')

    movies_df = cleaning.prepare_genres(movies_df)

    # get the list of all genres
    all_genres = extract.get_genres_list(movies_df)

    movies_df = movies_df.head(30000)

    # Get the tf-idf matrix
    tfidf_matrix = TfidfVectorizer(vocabulary=all_genres).fit_transform(movies_df['genres'])

    # get the similarity matrix
    cosine_df = pd.DataFrame(cosine_similarity(tfidf_matrix, tfidf_matrix))
    cosine_df.to_csv('the_matrix.csv')

    s3.upload_file('the_matrix.csv', 'pydatapipelinebucket', 'the_s3_matrix.csv')

    print("Finished!")

if __name__ == "__main__":
    prepare()

