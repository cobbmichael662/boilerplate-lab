#!/usr/bin/env python3
"""Entry point."""

import argparse

from utils import slugify


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Demo CLI")
    p.add_argument("text", nargs="?", default="Hello World")
    return p


def main() -> None:
    args = build_parser().parse_args()
    print(slugify(args.text))


if __name__ == "__main__":
    main()
