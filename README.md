# Chubby Cheekz — WoW Forever character tracker

Public snapshots for Chubby Cheekz (Americas, Normal/PvE).

The tracker uses the [WoW Forever Armory snapshot updater](https://github.com/stefan-mostert/wow-forever-armory), with local validation, automated tests, status reporting and hourly GitHub Actions updates. See [SPEC.md](SPEC.md).

## Character data

- [Chubby Cheekz profile JSON](chubby-cheekz.json) (available after first successful update)
- [Update status](update-status.json) (available after first update)
- [Workflow runs](../../actions/workflows/update-armory.yml)

## Run a check

Go to **Actions → Update Armory → Run workflow**, choose `main`, then run. Scheduled checks occur around minute 23 each hour UTC, subject to GitHub delays.

The updater reads the publicly available `https://armorywowforever.com/api/character/forever/us/normal/chubby-cheekz?refresh=1&lang=en`. No authentication credentials are required by the updater. Character data can still be cached upstream. The last good snapshot is preserved on failure.

To publish automatically, GitHub Actions must have permission to write repository contents; under **Settings → Actions → General → Workflow permissions**, choose read and write permissions if necessary.

Source implementation: [stefan-mostert/wow-forever-armory](https://github.com/stefan-mostert/wow-forever-armory).

## Quest history (optional addon)

See [QUEST_TRACKING.md](QUEST_TRACKING.md) for the WoW Forever quest-history addon, setup instructions and importer. The addon saves completed and active quest IDs locally; quest data is **not automatically uploaded** by the hourly Armory workflow. After converting and committing `quests-chubby-cheekz.json`, quest-aware recommendations can use it.

## Questing recommendations

- [Level 41 quest and dungeon route](LEVELING_GUIDE.md) — grouped from this character's active quest IDs
- [Active quest ID lookup](active-quest-catalog.json) — 27 quest names/zones matched, 12 IDs still unresolved in public references

These are snapshot-based recommendations, not an automatic quest-objective tracker. The addon still exports only accepted and completed IDs.

## Questing recommendations

- [Leveling and dungeon advisor](LEVELING_ADVISOR.md) — current questing route for Chubby Cheekz, grounded in saved quest history and level.
- [Active quest ID catalog](quest_catalog.json) — names, zones, relevant notes and source links for all 39 quests.

The recommendations are a researched snapshot rather than automatically regenerated every hour. Refresh quest history after playing to keep them accurate.

## Automatic leveling report

`build_leveling_advisor.py` regenerates [LEVELING_ADVISOR.md](LEVELING_ADVISOR.md) from the latest `chubby-cheekz.json`, `quests-chubby-cheekz.json` and `quest_catalog.json` on each successful updater publication. The workflow also starts when a new quest export or catalog change is committed to `main`.

Quest history is **not** automatically collected from the game: use `/cqt`, reload/log out, import and commit the new JSON. The report uses only the last uploaded quest history; it doesn't track objective counters, unlock unaccepted quests or verify dungeon difficulty. Changes in Armory fetchedAt metadata alone may trigger a report run but normally won't change the generated text.

Run locally with `python build_leveling_advisor.py`, or inspect the [Actions workflow](../../actions/workflows/update-armory.yml). Generation and tests are configured but a post-change workflow run has not yet been confirmed.
