"""Generate an evidence-limited leveling report from Armory and quest snapshots."""
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

PRIORITY = ["Stranglethorn Vale", "Drowned City", "Arathi Highlands",
            "Razorfen Downs", "Scarlet Monastery", "Riverglades"]

def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def stamp(value, milliseconds=False):
    if type(value) not in (int, float) or value < 0:
        return "unknown"
    ts = value / 1000 if milliseconds else value
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

def build(character, quests, catalog):
    if character.get("name") != "Chubby Cheekz" or quests.get("character") != "Chubby Cheekz":
        raise ValueError("Character identity mismatch")
    level = character.get("level")
    if type(level) is not int or not 1 <= level <= 60:
        raise ValueError("Invalid level")
    if quests.get("activeAvailable") is not True or quests.get("completedAvailable") is not True:
        raise ValueError("Quest history is not available")
    for field in ("active", "completed"):
        ids = quests.get(field)
        if not isinstance(ids, list) or any(type(i) is not int or i <= 0 for i in ids):
            raise ValueError("Invalid quest list: " + field)
        if len(set(ids)) != len(ids):
            raise ValueError("Duplicate quest IDs: " + field)
    active = set(quests["active"])
    completed = set(quests["completed"])
    if active & completed:
        raise ValueError("Quest IDs overlap across active and completed")
    rows = catalog.get("quests")
    if not isinstance(rows, list):
        raise ValueError("Missing quest catalog")
    lookup = {q["id"]: q for q in rows if type(q.get("id")) is int}
    groups = defaultdict(list)
    for quest_id in sorted(active):
        q = lookup.get(quest_id, {"id": quest_id, "name": "Unmapped quest",
                                 "zone": "Unknown", "type": "unknown",
                                 "note": "Requires manual lookup"})
        zone = q.get("zone", "Unknown").split(" → ")[-1]
        groups[zone].append(q)
    ordered = sorted(groups, key=lambda zone: (
        0 if zone in PRIORITY else 1,
        PRIORITY.index(zone) if zone in PRIORITY else -len(groups[zone]), zone))
    gear = {i.get("slot"): i.get("name") for i in character.get("items", [])}
    out = [
        "# Chubby Cheekz — leveling and dungeon advisor", "",
        "> Automatically generated from the latest published Armory data and manually exported quest history.",
        "> Quest objectives, exact dungeon suitability and rewards are not independently verified.", "",
        f"**Character:** level {level} {character.get('race', '')} {character.get('className', '')} · "
        f"{len(completed)} completed quests · {len(active)} active quests", "",
        f"**Armory fetched:** {stamp(character.get('fetchedAt'), True)} · "
        f"**Quest export saved:** {stamp(quests.get('updatedAt'))}", "",
        f"**Weapon:** {gear.get('MAIN_HAND') or 'not reported'} · "
        f"**Off-hand/shield:** {gear.get('OFF_HAND') or 'not reported'}", "",
        "## Suggested next areas", ""
    ]
    for zone in ordered[:5]:
        count = len(groups[zone])
        kind = "dungeon quests; confirm group suitability" if any(
            q.get("type") == "dungeon" for q in groups[zone]) else "combine nearby objectives"
        out.append(f"- **{zone}:** {count} active quest(s); {kind}.")
    out += ["", "## Active quests grouped by area", ""]
    for zone in ordered:
        out += [f"### {zone} ({len(groups[zone])})", ""]
        for q in sorted(groups[zone], key=lambda x: x["id"]):
            name = str(q.get("name") or "Unmapped quest").replace("[", "\\[").replace("]", "\\]")
            url = q.get("source", "")
            title = f"[{name}]({url})" if isinstance(url, str) and url.startswith("https://") else name
            note = str(q.get("note") or "No verified objectives").replace("\n", " ")
            out.append(f"- **{title}** (#{q['id']}): {note}")
        out.append("")
    missing = sorted(active - set(lookup))
    out += [
        "## Limitations", "",
        "- **Quest progress is not automatically synced.** Re-export with /cqt and commit the updated JSON.",
        "- Active quests may already have completed objectives awaiting turn-in; this export has no objective counters.",
        "- Catalog names, zones and notes are community-derived and must be checked in game.",
        "- This generator cannot discover new unaccepted quests or independently validate dungeon levels and rewards.",
        f"- Unmapped active quest IDs: {', '.join(map(str, missing)) if missing else 'none'}.", ""
    ]
    return "\n".join(out)

def main():
    root = Path(__file__).resolve().parent
    text = build(read(root / "chubby-cheekz.json"),
                 read(root / "quests-chubby-cheekz.json"),
                 read(root / "quest_catalog.json"))
    target = root / "LEVELING_ADVISOR.md"
    if not target.exists() or target.read_text(encoding="utf-8") != text:
        target.write_text(text, encoding="utf-8")
        print("Leveling advisor updated")
    else:
        print("Leveling advisor unchanged")

if __name__ == "__main__":
    main()
