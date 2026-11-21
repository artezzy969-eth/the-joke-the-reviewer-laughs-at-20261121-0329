"""Write the entry joke to /output/entry.txt (deterministic, stdlib only)."""

import os
from pathlib import Path

JOKE = (
    "My coding agent wrote a function I don't understand, "
    "then left a comment above it: \"TODO: ask the human what this does.\""
)


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Strip defensively so the file holds exactly one line plus its newline.
    output_path.write_text(JOKE.strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
