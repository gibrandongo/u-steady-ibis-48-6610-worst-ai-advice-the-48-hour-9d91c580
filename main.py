"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible advice, in the confident tidy
voice of an AI assistant, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: no clock, no network, no randomness.
"""

import os
import sys

# The advice: one original line, 140 characters or fewer.
ADVICE = (
    "To save on therapy, text your ex at 2 a.m. and ask what went wrong "
    "— closure is cheaper than a copay."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    line = ADVICE.strip()
    if not line or len(line) > 140 or "\n" in line or "\r" in line:
        print(
            "error: advice line must be a single non-empty line of "
            "at most 140 characters",
            file=sys.stderr,
        )
        return 1

    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(line + "\n")
        # Round-trip check: the file must read back as exactly one line.
        with open(path, "r", encoding="utf-8", newline="\n") as handle:
            content = handle.read()
        if content != line + "\n":
            print("error: written entry.txt does not match the advice line",
                  file=sys.stderr)
            return 1
    except OSError as exc:
        print(f"error: cannot write entry.txt: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
