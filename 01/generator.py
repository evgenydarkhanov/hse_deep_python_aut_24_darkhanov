import io
from typing import Union, List, Optional


def read_text(filename: Union[str, io.TextIOWrapper],
              search_words: List[str],
              stop_words: List[str]):
    
    if not isinstance(search_words, list):
        raise TypeError("'search_words' must be 'list'")

    if not isinstance(stop_words, list):
        raise TypeError("'stop_words' must be 'list'")

    if not all([isinstance(search_word, str) for search_word in search_words]):
        raise TypeError("'search_words' elements must be 'str'")

    if not all([isinstance(stop_word, str) for stop_word in stop_words]):
        raise TypeError("'stop_words' elements must be 'str'")

    if isinstance(filename, str):
        with open(filename, 'r') as file:
            for line in file:
                yield line

    elif isinstance(filename, io.TextIOWrapper):
        for line in filename:
            yield line

    else:
        raise TypeError("filename must be 'str' or 'io.TextIOWrapper'")


def check_line(line: str, search_words: List[str], stop_words: List[str]):
    line_lower = line.lower()

    for stop_word in stop_words:
        if line_lower.find(stop_word.lower()) != -1:
            return None

    for search_word in search_words:
        if line_lower.find(search_word.lower()) != -1:
            return line.rstrip()

    return None