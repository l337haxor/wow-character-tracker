-- Quest data is collected ONLY when the player enters /cqt.
-- Never scan quests during logout or quest-log events: those can fire while
-- the client is already busy persisting SavedVariables.
local function snapshot()
    if not C_QuestLog then
        return false, "The quest log API is unavailable."
    end

    local completed = {}
    local active = {}
    local completedAvailable = false
    local activeAvailable = false

    if type(C_QuestLog.GetAllCompletedQuestIDs) == "function" then
        local ids = C_QuestLog.GetAllCompletedQuestIDs()
        if type(ids) == "table" then
            completedAvailable = true
            for _, id in pairs(ids) do
                if type(id) == "number" and id > 0 then
                    completed[#completed + 1] = id
                end
            end
        end
    end

    if type(C_QuestLog.GetNumQuestLogEntries) == "function" and type(C_QuestLog.GetInfo) == "function" then
        activeAvailable = true
        for index = 1, C_QuestLog.GetNumQuestLogEntries() do
            local info = C_QuestLog.GetInfo(index)
            if info and not info.isHeader and type(info.questID) == "number" then
                active[#active + 1] = info.questID
            end
        end
    end

    if not completedAvailable and not activeAvailable then
        return false, "No supported quest data API is available."
    end

    table.sort(completed)
    table.sort(active)

    -- Only replace available data. Preserve previously captured quest history
    -- if an API is unavailable this session.
    ChubbyQuestTrackerDB = ChubbyQuestTrackerDB or {}
    local data = ChubbyQuestTrackerDB
    local playerName = UnitName("player") or ""
    data.character = (GetUnitName and GetUnitName("player", true)) or playerName
    data.realm = GetRealmName() or ""
    data.updatedAt = time()
    data.completedAvailable = completedAvailable
    data.activeAvailable = activeAvailable
    if completedAvailable then
        data.completed = completed
    end
    if activeAvailable then
        data.active = active
    end
    return true, tostring(#(data.completed or {})) .. " completed, " ..
        tostring(#(data.active or {})) .. " active"
end

SLASH_CHUBBYQUEST1 = "/cqt"
SlashCmdList.CHUBBYQUEST = function()
    local ok, message = snapshot()
    if not ok then
        print("|cffff5555ChubbyQuestTracker:|r " .. message)
        return
    end
    print("|cff00ccffChubbyQuestTracker:|r " .. message ..
        ". Snapshot stored in memory. Log out or /reload to save it to disk.")
end
