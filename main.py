"""Sum up 19 November 2026 world news in one image.

Deterministic, no network: copies the bundled front-page image
(entry.png, 1024x1024, under 1 MiB) to /output/entry.png.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path("/output/entry.png")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
