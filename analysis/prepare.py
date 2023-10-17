import boto3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pydata_engine_utils import cleaning,extract

def prepare():
    s3 = boto3.client('s3')

    s3.download_file('pydatapipelinebucket', 'all_movies.csv', 'local_file.csv')
    movies_df: pd.DataFrame = pd.read_csv('local_file.csv')

    # All the things
    movies_df = cleaning.prepare_genres(movies_df)

    # TODO - write out the cleaned data - maybe break up prep into two steps from here down
    print("Cleaned the dataset")
    # get the list of all genres
    all_genres = extract.get_genres_list(movies_df)

    movies_df = movies_df.head(30000)

    print("got the genres list")

    # Get the tf-idf matrix
    tf = TfidfVectorizer(vocabulary=all_genres)
    tfidf_matrix = tf.fit_transform(movies_df['genres'])

    print("tfidf-ed")

    # get the similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    cosine_df = pd.DataFrame(cosine_sim)
    print(f"cosine data frame exists with stuff {cosine_df.shape}")
    cosine_df.to_csv('the_matrix.csv')
    s3.upload_file('the_matrix.csv', 'pydatapipelinebucket', 'the_s3_matrix.csv')

    print("Finished!")

if __name__ == "__main__":
    prepare()

