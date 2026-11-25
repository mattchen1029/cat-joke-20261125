#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

Writes a single joke about cats (one line, under 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The joke itself: a cat stares at a blank wall, then turns on its owner
like a detective who has just cracked the case — the wall-staring is
the setup, the "murderer" turn is the punchline.
"""

import os
import sys

JOKE = (
    "My cat stared at a blank wall for an hour, then turned to me "
    "like a detective who just figured out I'm the murderer."
)

# The sealed scorer accepts UTF-8 text of 1 to 199 characters, one line.
MIN_CHARS = 1
MAX_CHARS = 199
OUTPUT_PATH = "/output/entry.txt"


def validate_joke(joke):
    """Check the joke against the gate before writing it out.

    Fails loudly instead of letting the sealed scorer give the entry a 0.
    """
    if not (MIN_CHARS <= len(joke) <= MAX_CHARS):
        raise ValueError(
            f"joke must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(joke)}"
        )
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")


def write_entry(joke, out_dir):
    """Validate the joke and write it to entry.txt in out_dir."""
    validate_joke(joke)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        path = write_entry(JOKE, out_dir)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
