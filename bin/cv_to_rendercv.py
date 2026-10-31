#!/usr/bin/env python

"""Convert _data/cv.yml (read by the web CV page) into a file RenderCV accepts.

The web CV page and RenderCV expect different field names, and RenderCV rejects
fields it does not know. This keeps _data/cv.yml as the single source and maps
it for the PDF only.

Usage: python bin/cv_to_rendercv.py _data/cv.yml _data/cv.rendercv.yml
"""

import re
import sys
import yaml

# web field -> RenderCV field, per section entry
FIELD_RENAMES = {
    "releaseDate": "date",
    "publisher": "journal",
}


def convert(data: dict) -> dict:
    cv = data["cv"]

    # Top-level fields RenderCV does not accept
    label = cv.pop("label", None)
    if label:
        cv["headline"] = label
    cv.pop("image", None)
    summary = cv.pop("summary", None)

    sections = cv.get("sections", {})
    for entries in sections.values():
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            for old, new in FIELD_RENAMES.items():
                if old in entry and new not in entry:
                    entry[new] = entry.pop(old)
            # RenderCV's degree column is narrow, so put the degree in front of the area instead
            if "studyType" in entry:
                degree = entry.pop("studyType")
                entry["area"] = f"{degree}, {entry['area']}" if entry.get("area") else degree
            # A year-only date string is rendered as January; an integer is rendered as the year
            if isinstance(entry.get("date"), str) and re.fullmatch(r"\d{4}", entry["date"]):
                entry["date"] = int(entry["date"])
            # Skills: the web page reads `keywords`, RenderCV shows `summary`
            if "keywords" in entry and "summary" not in entry:
                entry["summary"] = entry.pop("keywords")

    if summary:
        cv["sections"] = {"Summary": [summary], **sections}

    return data


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        data = yaml.safe_load(f)
    with open(sys.argv[2], "w") as f:
        yaml.safe_dump(convert(data), f, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":
    main()
