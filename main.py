#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh — make.fun entry.

Writes the graded one-line safety warning label to entry.txt next to
this file. Pure Python standard library, no network, no input files.

The label: this human operates on caffeine, spite, and sleep it never
got — do not shake, and do not ask how it is doing before coffee.
Funny first, plausible second, in the wording of a real warning label.
"""

import os

ENTRY = "WARNING: This human operates on caffeine, spite, and sleep it never got. Do not shake. Do not ask how it is doing before coffee."

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    path = os.path.join(HERE, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Grading sandbox: the scorer reads /output/entry.txt, collected as
    # another user, so the copy there must be world-readable (mode 0644).
    out_dir = "/output"
    if os.path.isdir(out_dir):
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(out_path, 0o644)
    print("Wrote %d chars: %r" % (len(ENTRY), ENTRY))


if __name__ == "__main__":
    main()
