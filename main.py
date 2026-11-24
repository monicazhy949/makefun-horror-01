"""Two-Sentence Horror — entry program.

Writes one original two-sentence horror story to /output/entry.txt.
"""

import os

ENTRY = (
    "Every night my daughter asks me to check under her bed, "
    "and every night I tell her there is nothing there. "
    "Tonight she asked me to check behind me, "
    "and the voice that answered 'nothing there' was not mine."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
