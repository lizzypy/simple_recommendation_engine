from typing import List, Set

import pandas as pd


def lower_case_and_strip_spaces(input: str) -> str:
    return input.lower().strip()


def combine_genres_list(input: List[str]) -> Set:
    all_genres: Set = set()
    for genre_strings in input:
        genres: List[str] = genre_strings.split('|')
        for genre in genres:
            all_genres.add(genre)
    return all_genres

