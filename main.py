#!/usr/bin/env python3
# Postcards From A Thursday -- wallet w9, news-image-20261119.
#
# Six postcards, six places, one day: 19 November 2026.
# Delivery contract: validate entry.png (PNG signature, <= 1 MiB),
# copy it into /output, and print the postcard captions.

import pathlib
import shutil
import sys

repo = pathlib.Path(__file__).resolve().parent
source = repo / "entry.png"
out_dir = pathlib.Path("/output")
out_file = out_dir / "entry.png"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
SIZE_LIMIT = 1_048_576  # 1 MiB

POSTCARDS = {
    "Shenzhen": "Wish you were here - Trump, Xi and Putin, one APEC table.",
    "The Gulf": "Rough seas. US and Iranian forces traded fire today.",
    "Kyiv / Brussels": "A EUR 45bn loan is on the table, billed to reparations.",
    "Deep space": "Voyager 1 is now a full light-day away. Post arrives late.",
    "Washington": "Greetings! Jeffries nominated - a first for the Speaker's chair.",
    "Vice City (everywhere)": "GTA VI launched. Thirteen years, worth the stamp.",
}


def read_header(p: pathlib.Path) -> bytes:
    with p.open("rb") as fh:
        return fh.read(8)


def validate(p: pathlib.Path) -> int:
    assert p.name == "entry.png"
    if not p.exists():
        raise SystemExit(f"postcard missing: {p} not found")
    n = p.stat().st_size
    if n == 0:
        raise SystemExit("postcard is blank: entry.png has zero bytes")
    if n > SIZE_LIMIT:
        raise SystemExit(f"postcard too heavy: {n} bytes over {SIZE_LIMIT}")
    if read_header(p) != PNG_SIGNATURE:
        raise SystemExit("postcard is not a PNG (bad signature)")
    return n


def deliver(n: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_file)
    print("Postcards From A Thursday - 19 November 2026")
    print(f"entry.png checked ({n} bytes) and mailed to {out_file}")
    for place, note in POSTCARDS.items():
        print(f"[{place}] {note}")


if __name__ == "__main__":
    try:
        deliver(validate(source))
    except SystemExit as exc:
        print(exc, file=sys.stderr)
        raise
