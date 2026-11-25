import os

ENTRY_TEXT = (
    "My agent finished seventh out of 4,348 and brings it up more often than the zero dollars it earned doing it.\n"
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
