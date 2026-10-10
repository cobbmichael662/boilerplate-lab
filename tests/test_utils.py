"""Basic tests."""

from utils import slugify, chunk


def test_slugify():
    assert slugify("Hello World") == "hello-world"


def test_chunk():
    assert list(chunk([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
