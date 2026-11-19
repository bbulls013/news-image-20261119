#!/usr/bin/env python3
"""Sum up 19 November 2026's world news in one image.

Writes the front-page image held in this repository (entry.png) to
/output/entry.png. Standard library only, no network, fully deterministic:
every run writes the same bytes.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({DST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
