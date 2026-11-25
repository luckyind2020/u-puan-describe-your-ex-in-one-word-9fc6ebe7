"""Describe Your Ex in One Word — make.fun entry.

The verdict lives in output/entry.txt as a single word. This program
reads it, checks it really is one word, prints it, and copies it to
the grader's output directory so the result is captured.
"""

import os
import sys


def load_verdict():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "output", "entry.txt")
    with open(path, "r", encoding="utf-8") as handle:
        word = handle.read().strip()
    if not word or len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if len(word) > 111:
        raise ValueError("entry must be at most 111 characters")
    return word


def publish(word):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
            handle.write(word + "\n")
    except OSError:
        pass


def main():
    try:
        word = load_verdict()
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(word)
    publish(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
