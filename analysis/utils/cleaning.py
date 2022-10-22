from typing import List, Set

import pandas as pd


def lower_case_and_strip_spaces(input: str) -> str:
    return input.lower().strip()


def combine_genres_list(input: List[str]) -> str:
    all_genres: List = []
    for genre_string in input:
        list_of_genres: List = genre_string.split('|')
        for genre in list_of_genres:
            if genre not in all_genres:
                all_genres.append(genre)

    return '|'.join(all_genres)

