"""Small reusable helpers."""

from typing import Iterable, Iterator


def slugify(text: str) -> str:
    """Lowercase and replace whitespace runs with single dashes."""
    return "-".join(text.lower().split())


def chunk(items: Iterable, size: int) -> Iterator[list]:
    """Yield successive lists of `size` from `items`."""
    buf = []
    for item in items:
        buf.append(item)
        if len(buf) == size:
            yield buf
            buf = []
    if buf:
        yield buf


def read_lines(path: str) -> list:
    """Read a text file, stripping trailing newlines."""
    with open(path, "r", encoding="utf-8") as fh:
        return [line.rstrip("\n") for line in fh]
