# Chubby Cheekz — Questing and dungeon plan (level 41)

Snapshot date: 19 November 2026. This plan uses `quests-chubby-cheekz.json` (492 completed; 39 active) and the character's last checked Armory snapshot (level 41 Troll Warrior). It is a **snapshot**, not a real-time view of quest objective progress. Recheck your in-game journal before travelling. Public quest sites mix verified Forever records with Classic references.

## Data status

- `active-quest-catalog.json`: **27 IDs mapped** to public quest names and coarse zones, **12 unresolved or partially identified** new/high-numbered Forever IDs.
- This is an advisory layer; it does not overwrite or falsely mark any quests complete.
- Quest-log objectives, completion percentages and turn-in readiness are **not** in the current addon export, so the route is based on accepted quests and zone groupings rather than exact remaining tasks.
- The uncertain IDs are `79236, 94930, 95141, 95143, 95144, 95773, 95775, 95789, 95791, 96774, 97196, 97884`. The public ForeverDB record for 95791 confirms a level-40 quest with rewards but does not establish its name or location.

## Prioritized plan

1. **Stranglethorn Vale (best immediate consolidation).** You have ten familiar Stranglethorn-related quests active. Combine [Raptor Mastery #196](https://questing.wiki/wow-forever/quests/196/), [Skullsplitter Tusks #209](https://questing.wiki/wow-forever/quests/209/), [Mok'thardin's Enchantment #572](https://questing.wiki/wow-forever/quests/572/), [The Bloodsail Buccaneers #595](https://questing.wiki/wow-forever/quests/595/) and [Scaring Shaky #606](https://questing.wiki/wow-forever/quests/606/) with nearby objectives. Also check Hostile Takeover #213, Green Hills #338, Some Assembly Required #577, Singing Blue Shards #605. Don't deliberately travel to Hinterlands solely for [Whiskey Slim's Lost Grog #580](https://questing.wiki/wow-forever/quests/580/) (quest level 50); defer it until a Hinterlands trip.
2. **Arathi Highlands (second clustered trip).** You hold [Sigil of Trollbane #644](https://questing.wiki/wow-forever/quests/644/), [Call to Arms #679](https://questing.wiki/wow-forever/quests/679/), [The Real Threat #680](https://questing.wiki/wow-forever/quests/680/), [Guile of the Raptor #701](https://questing.wiki/wow-forever/quests/701/), [Crystal in the Mountains #635](https://questing.wiki/wow-forever/quests/635/), [Sunken Treasure #670](https://questing.wiki/wow-forever/quests/670/) and [Theldurin the Lost #687](https://questing.wiki/wow-forever/quests/687/). Group the Hammerfall/Arathi tasks. Some are chains or travel steps; confirm the quest journal before attempting a difficult area.
3. **Dungeon day (level-appropriate).** [Into the Scarlet Monastery #1048](https://questing.wiki/wow-forever/quests/1048/) is still **active**, even though your Armory shows Vanquisher's Sword. Verify which of Loksey, Herod, Mograine and Whitemane remain; finish the quest and turn it in rather than automatically assuming it's done. At level 41, Scarlet Monastery Cathedral (range roughly 38–46), Razorfen Downs (37–46), and the new Krol'dok Stronghold (40–45) are reasonable options. Uldaman (41–51) is possible, but deeper pulls can be hard on a level-41 tank. [An Unholy Alliance #6521](https://questing.wiki/wow-forever/quests/6521/) is related to Razorfen Downs.
4. **Profession / Warrior detours.** [Barbaric Battlements #2751](https://questing.wiki/wow-forever/quests/2751/) is a Blacksmithing quest in Orgrimmar. [Cyclonian #1712](https://questing.wiki/wow-forever/quests/1712/) is an older Warrior Whirlwind weapon quest: since you're sword-and-shield with Vanquisher's Sword, finish it only for completion or a specific reward, not as a one-handed weapon upgrade. [Satyr Hooves #1842](https://questing.wiki/wow-forever/quests/1842/) and [Dragonmaw Shinbones #1846](https://questing.wiki/wow-forever/quests/1846/) belong to older Warrior equipment quest chains; prioritize only if you still need their rewards.
5. **Travel and cleanup.** [Martek the Exiled #1106](https://questing.wiki/wow-forever/quests/1106/) goes to Badlands; [Dream Dust in the Swamp #1116](https://questing.wiki/wow-forever/quests/1116/) and [Razzeric's Tweaking #1187](https://questing.wiki/wow-forever/quests/1187/) involve Dustwallow. Blackfathom Villainy #6561 is a low-level dungeon quest—usually not worthwhile to deliberately return for XP at 41.

## Getting to level 45

Once the clustered accepted quests dry up, Forever-specific **Riverglades** (quests 40–45), **Shen'dralas** (early 40s), Feralas and eventually Tanaris provide more options. These are **new options**, not confirmed available quests on your character; don't assume prerequisite completion. A zone guide reports 74 Horde quests at levels 40–45 in Riverglades, although not all will be immediately accessible.

Dungeon level references:
- https://www.wowhead.com/forever/guide/dungeons-overview-locations-details
- https://foreverchanges.pro/dungeons

Leveling-zone references:
- https://www.hardcorehelper.com/forever/guides/wow-forever-leveling-guide-40-45
- https://theforeverera.com/en/guides/leveling/

## Next data upgrade (not implemented)

The quest addon currently exports only IDs. To plan exact objective order and know whether a quest is ready to turn in, extend the addon to include quest title, zone/category, objective descriptions, quantity progress and completion flag, with an explicit `/cqt` scan only. Test any update on a backup of the functioning addon to avoid another client freeze. Automated syncing of the local SavedVariables file to GitHub remains **unimplemented**.
