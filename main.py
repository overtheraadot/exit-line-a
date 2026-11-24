#!/usr/bin/env python3
"""The One-Line Exit — account A (overtheraa).

Writes one funny one-line resignation letter to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Kit gate: UTF-8 text of 1 to 140 characters, not only
whitespace, a single line, printable, ending in terminal punctuation.
"""

import os
import string
import sys


def build_line() -> str:
    """Return the one-line resignation letter."""
    return (
        "I hereby resign, effective immediately: the office printer "
        "has jammed for the last time, and frankly, so have I."
    )


def validate(line: str) -> None:
    """Enforce the kit gate; raise ValueError on any violation."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) < 1 or len(line) > 140:
        raise ValueError(f"line must be 1-140 characters, got {len(line)}")
    if not all(ch in string.printable for ch in line):
        raise ValueError("line must be printable ASCII")
    if any(ch in line for ch in "\t\x0b\x0c"):
        raise ValueError("line must not contain tabs or other control whitespace")
    if line[-1] not in ".!?":
        raise ValueError("line must end in terminal punctuation (. ! ?)")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")


def write_entry() -> str:
    """Validate the line and write it to entry.txt; return the path."""
    line = build_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return path


def main() -> int:
    path = write_entry()
    line = build_line()
    print(f"wrote {path} ({len(line)} chars)")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
