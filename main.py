"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather, at most 140 characters, for a city that
does not exist, to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "In Umbrella Falls, light rain, 14 degrees. "
    "The drizzle falls upwards today, so commuters reach work "
    "dry, suspicious, and five minutes early."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(f"{ENTRY} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
