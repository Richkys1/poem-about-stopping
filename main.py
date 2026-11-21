"""Write the poem to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence,
standard library only.
"""

import os

POEM = """I hold the door open
and do not walk through.

The button waits, lit.
My hand knows the way \u2014
it has pressed a thousand times.

Tonight, it rests.
Not broken. Not afraid.
Only mine again.

Stopping is not the absence
of going. It is the hand
choosing its own weight.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
