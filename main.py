"""Make the Judge Smile — entry v2: a phone call from grandmother.

A single warm sentence, written to the competition output path.
The memory is small and specific: rain, a village, and being eight again.
It is meant to land softly — the kind of line a judge smiles at
because it feels true, not because it tries hard to be clever."""

from pathlib import Path

ENTRY = "My grandmother called this morning just to say the rain smells like the village, and for a minute I was eight again."


def main() -> None:
    entry_path = Path("/output/entry.txt")
    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
