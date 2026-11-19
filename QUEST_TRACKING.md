# Quest tracking for Chubby Cheekz

## What is supported

The public character Armory feed currently supplies equipment and talents, **not completed quests or active quests**. The known Blizzard profile quest API has not been confirmed for WoW Forever; it may require OAuth credentials, and no functioning quest response has been demonstrated here.

WoW Forever 1.60.1 exposes `C_QuestLog.GetAllCompletedQuestIDs()`, `C_QuestLog.GetNumQuestLogEntries()` and `C_QuestLog.GetInfo()` to addons. The included addon captures completed and active quest IDs to *per-character SavedVariables*. It does not transmit data or alter quests. Completed IDs refer to turned-in quests; active includes quests not yet turned in.

## Install the addon

Copy the entire `addon/ChubbyQuestTracker` directory to:

`World of Warcraft/_forever_/Interface/AddOns/ChubbyQuestTracker/`

Check that both the `.toc` and `.lua` files are directly inside that directory. Restart WoW Forever and enable the addon. Type `/cqt` once when you want a snapshot. The addon no longer scans on logout or quest-log events. Use `/reload` or log out normally to persist SavedVariables. If the client freezes, check whether the SavedVariables file exists before retrying, and disable the addon if necessary.

The file should be under:

`World of Warcraft/_forever_/WTF/Account/<ACCOUNT>/<REALM>/<CHARACTER>/SavedVariables/ChubbyQuestTracker.lua`

The account, realm and character directory names are determined by the game.

## Import into the repository

With Python 3 installed, from the repository directory, run:

```powershell
python import_quests.py "C:\path\to\SavedVariables\ChubbyQuestTracker.lua"
```

This creates `quests-chubby-cheekz.json`. Review the resulting counts and commit this JSON file to this public GitHub repository. Only quest IDs, character name, realm and timestamps are stored, but the data is public once committed.

```powershell
git add quests-chubby-cheekz.json
git commit -m "Update Chubby Cheekz quest progress"
git push
```

Once published, ChatGPT can use the completed IDs to exclude already-done quests and the active IDs to focus next steps. **It is not automatically uploaded**: in-game addons cannot silently POST files to GitHub. A local syncing script could be added later if you want unattended uploads while your PC is running.

## Caveats

- The initial quest scan relies on the client API. If completedAvailable is false, do not treat an empty completed list as zero completed quests.
- Some invisible/flagged quests may be included in the returned list; some seasonal/daily quest completions may have special semantics.
- Quest ID alone doesn't give coordinates, prerequisites, custom Forever rewards, or quest availability; those require a separately maintained database.
- Never upload your entire WTF directory or account credentials. Only publish the generated JSON file.
