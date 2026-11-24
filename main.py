"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 characters) pitching a bizarre startup idea
that sounds absurd until you realise it would actually sell, to
/output/entry.txt. Pure stdlib, no network, no input files.
"""

import os

ENTRY = (
    "We sell tiny funerals for dead houseplants: guilty owners pay $19 "
    "for a coffin, a eulogy and composting, because grief outlives the fern."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, not only
    # whitespace, and exactly one sentence. A trailing newline is not added,
    # so the file holds exactly the pitched sentence and nothing else.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1..200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
