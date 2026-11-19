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
