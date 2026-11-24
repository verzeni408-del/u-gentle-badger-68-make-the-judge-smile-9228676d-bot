"""v3 — Make the Judge Smile.

A quiet morning moment: the barista sketches a lopsided heart on
the coffee cup, and that small wobbly gesture ends up being the
one steady, warm thing in an otherwise unsteady day.
"""

from pathlib import Path

ENTRY = "The barista drew a crooked heart on my cup this morning, and it was the steadiest thing all day."


def main():
    # Write the single-line entry to the expected output path.
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
