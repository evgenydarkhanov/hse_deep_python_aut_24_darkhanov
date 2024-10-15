import json
from collections.abc import Callable
from typing import Optional


def process_json(
    json_str: str,
    required_keys: Optional[list[str]] = None,
    tokens: Optional[list[str]] = None,
    callback: Optional[Callable[[str, str], None]] = None,
) -> None:

    if not isinstance(json_str, str):
        raise TypeError("json_str must be 'str'")

    if required_keys is None or tokens is None:
        return None

    # исключение может выброситься автоматически
    json_parsed = json.loads(json_str)

    for key in json_parsed.keys():
        if key in required_keys:
            values = json_parsed[key].lower().split()
            for token in tokens:
                if token.lower() in values:
                    if callback is not None:
                        callback(key, token)
    return None
