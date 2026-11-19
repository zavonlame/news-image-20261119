"""Sum up 19 November 2026 world news in one image.

Deterministic, no network: copies the bundled front-page image
(entry.png, 1024x1024, under 1 MiB) to /output/entry.png.
The image is a dense newspaper front page: masthead, hero
Trump-Xi-Putin summit in Shenzhen, and nine world briefs.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path("/output/entry.png")


def main() -> None:
    if not SRC.is_file():
        raise FileNotFoundError(f"bundled image missing: {SRC}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    assert OUT.is_file()


if __name__ == "__main__":
    main()
