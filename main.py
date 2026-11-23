"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is not set). The line is 1-200 characters, UTF-8, not only whitespace.
"""

import os

LINE = (
    "My fitness app congratulated me on 10,000 steps today, "
    "all I did was lose my keys three times inside my own house."
)


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(text)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
