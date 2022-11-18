import io
from typing import Iterable


def join(sep: str, iterable: Iterable[str], /) -> str:
    """
    A str.join replacement.

    Concatenate any number of strings.

    The string `sep` is inserted in between each given string.
    The result is returned as a new string.

    Example: join('.', ['ab', 'pq', 'rs']) -> 'ab.pq.rs'
    """
    result = io.StringIO(newline='')  # Do not translate newlines
    iterator = iter(iterable)
    first = next(iterator, None)
    if first:
        # Skip first separator
        result.write(first)
    for remaining in iterator:
        result.write(sep)
        result.write(remaining)
    return result.getvalue()
