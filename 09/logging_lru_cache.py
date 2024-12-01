import argparse
import logging
from collections.abc import Hashable


def create_logger(filename, classname):
    """ creates a new logger with a file handler """
    new_logger = logging.getLogger(name=filename)
    new_logger.setLevel(logging.DEBUG)
    new_logger.propagate = False

    while new_logger.handlers:
        new_logger.removeHandler(new_logger.handlers[-1])

    file_handler = logging.FileHandler(f"{filename}.log", mode="w")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "FILE\t%(levelname)s\t%(message)s"
        )
    )

    new_logger.addHandler(file_handler)
    new_logger.debug("created %s instance", classname)
    new_logger.debug("created log file '%s.log'", filename)

    return new_logger


def create_stream_handler(logger_name):
    """ creates and adds a new stream handler """
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(
        logging.Formatter(
            "STREAM\t%(levelname)s\t%(message)s"
        )
    )
    logger_name.addHandler(stream_handler)


def custom_filter(record):
    """ отбрасывает записи c нечетным числом слов """
    return len(record.msg.split()) % 2 == 0


class LRUCache:
    def __init__(self, limit=42, filename="cache"):
        if not isinstance(limit, int):
            raise TypeError("limit must be 'int'")
        if limit < 0:
            raise ValueError("limit must be positive")
        self.limit = limit
        self.cache = {}
        self.logger = create_logger(filename, self.__class__.__name__)

    def get(self, key):
        if not isinstance(key, Hashable):
            raise KeyError("key must be hashable")

        if key in self.cache:
            self.logger.info("getting existing key '%s'", key)    # logging

            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value

        self.logger.info("getting nonexistent key '%s'", key)     # logging
        return None

    def set(self, key, value):
        if not isinstance(key, Hashable):
            raise KeyError("key must be hashable")

        if key in self.cache:
            self.logger.info("setting existing key '%s'", key)    # logging
            del self.cache[key]
            self.cache[key] = value

        else:
            self.logger.info("setting nonexistent key '%s'", key)  # logging

            if len(self.cache) == self.limit:
                self.logger.info("limit reached")               # logging
                del self.cache[next(iter(self.cache))]

            self.cache[key] = value


def process_args():
    parser = argparse.ArgumentParser(description="LRU Cache with logging")
    parser.add_argument('-s', action='store_true', help='stdout logging')
    parser.add_argument('-f', action='store_true', help='custom filtration')
    args = parser.parse_args()
    return args


def main():
    args = process_args()
    cache = LRUCache(2)

    if args.s:
        create_stream_handler(cache.logger)
        cache.logger.debug("created STREAM HANDLER")

    if args.f:
        for handler in cache.logger.handlers:
            cache.logger.debug("created FILTER %s", handler)
            handler.addFilter(custom_filter)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

    cache.set("k3", "val3")

    assert cache.get("k3") == "val3"
    assert cache.get("k2") is None
    assert cache.get("k1") == "val1"


if __name__ == "__main__":
    main()
