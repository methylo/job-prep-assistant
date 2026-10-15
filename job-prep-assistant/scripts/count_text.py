#!/usr/bin/env python3
"""Count the exact submission text; default includes LF as one character."""
import argparse
import json
import unicodedata
from pathlib import Path

def count(text):
    text = unicodedata.normalize("NFC", text.replace("\r\n", "\n").replace("\r", "\n"))
    return {"with_spaces": len(text), "without_whitespace": sum(not c.isspace() for c in text), "utf8_bytes": len(text.encode("utf-8"))}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--basis", choices=["with-spaces", "without-whitespace"], default="with-spaces")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 0:
        parser.error("limit must be nonnegative")
    result = count(args.file.read_text(encoding="utf-8"))
    result["basis"] = args.basis
    result["limit"] = args.limit
    result["within_limit"] = None if args.limit is None else result[args.basis.replace("-", "_")] <= args.limit
    print(json.dumps(result, ensure_ascii=False))
