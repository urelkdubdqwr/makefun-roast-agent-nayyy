"""Write the make.fun entry text to entry.txt in the output directory.

Standard library only. No network, randomness, clock reads, or extra output.
"""

import os
import sys

ENTRY_TEXT = (
    "My agent finished seventh out of 4,348 and brings it up more often than the zero dollars it earned doing it.\n"
)


def resolve_output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    output_dir = resolve_output_dir()
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as error:
        sys.stderr.write(f"could not create output directory {output_dir!r}: {error}\n")
        return 1
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
