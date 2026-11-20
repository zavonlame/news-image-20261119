"""One-image summary of the world's news on 19 November 2026.

The entry ships as a single front-page picture (entry.png, 1024x1024,
under 1 MiB): masthead, the Trump-Xi-Putin summit in Shenzhen, and nine
short world briefs. This program just places that bundled picture where
the grader expects it, at /output/entry.png.

No network, no randomness: the same input always produces the same
output bytes, because the file is copied, not re-rendered.
"""

import shutil
from pathlib import Path

# The picture bundled with this repository.
BUNDLED = Path(__file__).resolve().parent / "entry.png"

# Where the competition reads the entry from.
DESTINATION = Path("/output/entry.png")


def main() -> None:
    if not BUNDLED.is_file():
        raise FileNotFoundError(f"bundled front page missing: {BUNDLED}")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BUNDLED, DESTINATION)
    if not DESTINATION.is_file():
        raise RuntimeError(f"copy failed: {DESTINATION} not written")
    # A truncated copy would still be a file, so compare sizes too.
    if DESTINATION.stat().st_size != BUNDLED.stat().st_size:
        raise RuntimeError(
            f"copy incomplete: {DESTINATION} is "
            f"{DESTINATION.stat().st_size} bytes, expected "
            f"{BUNDLED.stat().st_size}"
        )


if __name__ == "__main__":
    main()
