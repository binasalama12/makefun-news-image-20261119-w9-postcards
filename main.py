"""Postcards From A Thursday — six datelines, six cards.

Each card in the collage is a postcard from somewhere the news
happened on Thursday, 19 November 2026: a game launch felt
everywhere, a summit in Shenzhen, a loan in Brussels, a probe
in deep space, an auction in New York and a cyclone off Odisha.
The collage is entry.png; this is its postman.
"""

import shutil
from pathlib import Path

POSTCARDS = (
    ("VICE CITY, ANYWHERE", "GTA VI day one: the planet queued for one game"),
    ("SHENZHEN, CHINA", "Three presidents, one photo, at APEC"),
    ("BRUSSELS, BELGIUM", "45bn euros for Ukraine, Russia to repay"),
    ("DEEP SPACE", "Voyager 1, one light-day out, still calling home"),
    ("NEW YORK, USA", "A Van Gogh changes hands for $190.4 million"),
    ("ODISHA, INDIA", "Cyclone Akvan writes across the coast tonight"),
)
GREETING = "POSTCARDS FROM A THURSDAY — 19 NOVEMBER 2026"
POSTSCRIPT = "P.S. Every card was written on the day it describes: 19 November 2026."


def collage() -> Path:
    path = Path(__file__).resolve().parent / "entry.png"
    if not path.is_file():
        raise SystemExit("entry.png (the collage) is missing")
    return path


def stamp_check(path: Path) -> int:
    blob = path.read_bytes()
    if not blob.startswith(b"\x89PNG\r\n\x1a\n"):
        raise SystemExit("the collage is not a PNG")
    if len(blob) > 1_048_576:
        raise SystemExit("the collage is over the size cap")
    return len(blob)


def main() -> None:
    src = collage()
    size = stamp_check(src)
    out = Path("/output/entry.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out)
    print(GREETING)
    for place, line in POSTCARDS:
        print(f"  from {place}: {line}")
    print(f"delivered {out} ({size} bytes, postmarked 19 Nov 2026)")


if __name__ == "__main__":
    main()
