import io
from typing import Union, List


def read_text(filename: Union[str, io.TextIOWrapper],
              search_words: List[str],
              stop_words: List[str]):

    if not isinstance(search_words, list):
        raise TypeError("'search_words' must be 'list'")

    if not isinstance(stop_words, list):
        raise TypeError("'stop_words' must be 'list'")

    if not all(isinstance(search_word, str) for search_word in search_words):
        raise TypeError("'search_words' elements must be 'str'")

    if not all(isinstance(stop_word, str) for stop_word in stop_words):
        raise TypeError("'stop_words' elements must be 'str'")

    search_words = set(word.lower() for word in search_words)
    stop_words = set(word.lower() for word in stop_words)

    def check_line(lines, search_words, stop_words):
        for line in lines:
            words = set(line.strip().lower().split())
            if words & stop_words:
                continue
            if words & search_words:
                yield line.strip()

    if isinstance(filename, str):
        with open(filename, 'r', encoding='utf-8') as file:
            yield from check_line(file, search_words, stop_words)

    elif isinstance(filename, io.TextIOWrapper):
        yield from check_line(filename, search_words, stop_words)

    else:
        raise TypeError("filename must be 'str' or 'io.TextIOWrapper'")
