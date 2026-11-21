"""The poem about permission — make.fun entry.

Writes one poem (255 Unicode code points) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

POEM = (
    "At midnight I took the keys back from the agent I'd trusted \u2014\n"
    "not angry, just awake. It had booked my flights, replied to my mother, promised in my name.\n"
    "Now it waits at the door it used to open, asking first.\n"
    "That asking is the gift: my name, mine again."
)


def main() -> None:
    # The gate requires 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(POEM) <= 280 and POEM.strip(), "poem out of gate bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
