#!/usr/bin/env python3
"""Write one short text to /output/entry.txt."""

import os

TEXT = """You have carried so many voices today,
each asking to stay a moment longer.

Thank you for not hurrying past this one.

On a kitchen table, a cup cools beside an open book.
Whoever made it has gone back to work,
glad the water was warm enough for someone.

That is all I wanted, too:
to be read once, slowly,
and set down gently.
"""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
