#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

Writes a single joke about cats (one line, under 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

JOKE = (
    "My cat stared at a blank wall for an hour, then turned to me "
    "like a detective who just figured out I'm the murderer."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
