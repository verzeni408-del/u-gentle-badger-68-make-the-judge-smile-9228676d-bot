"""Write the entry that makes the judge smile to the absolute output path."""

import pathlib


def main():
    output_file = pathlib.Path("/output/entry.txt")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        "The street vendor slipped an extra fried banana into my bag and winked like it was our secret.",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
