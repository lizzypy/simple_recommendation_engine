from typing import List

def one_hot_encode_genres(all_genres_list, genres_list):
    one_hot_encoding: List = []

    for genre in all_genres_list:
        if genre in genres_list:
            one_hot_encoding.append(1)
        else:
            one_hot_encoding.append(0)

    return one_hot_encoding