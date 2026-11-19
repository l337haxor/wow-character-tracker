"""Convert ChubbyQuestTracker's WoW SavedVariables into a quest JSON snapshot.

The parser only accepts the small generated subset of Lua table syntax; it does not
execute Lua or accept arbitrary file paths embedded in the source.
"""
import argparse
import json
from pathlib import Path
import re

MAX_BYTES = 2 * 1024 * 1024

def scalar(source, field):
    pattern = r'\[?"?' + re.escape(field) + r'"?\]?\s*=\s*("([^"\\]|\\.)*"|true|false|[0-9]+)'
    matches = re.findall(pattern, source)
    if not matches:
        raise ValueError("Missing field: " + field)
    raw = matches[0][0]
    if raw in ("true", "false"):
        return raw == "true"
    if raw.startswith('"'):
        return json.loads(raw)
    return int(raw)

def ids(source, field):
    pattern = r'\[?"?' + re.escape(field) + r'"?\]?\s*=\s*\{([^{}]*)\}'
    match = re.search(pattern, source, re.DOTALL)
    if not match:
        raise ValueError("Missing ID array: " + field)
    body = match.group(1).strip()
    if not body:
        return []
    # SavedVariables writes numeric array entries as [1] = 123 or simply 123.
    entries = re.findall(r'(?:\[\s*\d+\s*\]\s*=\s*)?(\d+)\s*,?', body)
    if re.sub(r'(?:\[\s*\d+\s*\]\s*=\s*)?\d+\s*,?\s*', '', body):
        raise ValueError("Unrecognized entries in " + field)
    return sorted({int(i) for i in entries if int(i) > 0})

def parse(source):
    if not source.strip().startswith("ChubbyQuestTrackerDB"):
        raise ValueError("Not a ChubbyQuestTracker SavedVariables file")
    completed_available = scalar(source, "completedAvailable")
    active_available = scalar(source, "activeAvailable")
    return {
        "schema": 1,
        "source": "ChubbyQuestTracker SavedVariables",
        "character": scalar(source, "character"),
        "realm": scalar(source, "realm"),
        "updatedAt": scalar(source, "updatedAt"),
        "completedAvailable": completed_available,
        "activeAvailable": active_available,
        "completed": ids(source, "completed") if completed_available else [],
        "active": ids(source, "active") if active_available else [],
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("saved_variables", type=Path)
    parser.add_argument("--output", type=Path, default=Path("quests-chubby-cheekz.json"))
    args = parser.parse_args()
    if args.saved_variables.stat().st_size > MAX_BYTES:
        raise SystemExit("Input file too large")
    data = parse(args.saved_variables.read_text(encoding="utf-8-sig"))
    if "chubby" not in data["character"].casefold() or "cheekz" not in data["character"].casefold():
        raise SystemExit("Unexpected character; refusing to overwrite Chubby Cheekz's snapshot")
    args.output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {args.output}: {len(data['completed'])} completed, {len(data['active'])} active; "
          f"completedAvailable={data['completedAvailable']}")

if __name__ == "__main__":
    main()
