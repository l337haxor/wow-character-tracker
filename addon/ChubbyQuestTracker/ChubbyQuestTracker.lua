local addon = CreateFrame("Frame")
local function snapshot()
    if not C_QuestLog then
        return
    end

    ChubbyQuestTrackerDB = ChubbyQuestTrackerDB or {}
    local data = ChubbyQuestTrackerDB
    local playerName = UnitName("player") or ""
    local fullName = GetUnitName and GetUnitName("player", true) or playerName

    data.character = fullName
    data.realm = GetRealmName() or ""
    data.updatedAt = time()
    data.completed = {}
    data.active = {}

    if type(C_QuestLog.GetAllCompletedQuestIDs) == "function" then
        local ids = C_QuestLog.GetAllCompletedQuestIDs()
        if type(ids) == "table" then
            for _, id in pairs(ids) do
                if type(id) == "number" then
                    table.insert(data.completed, id)
                end
            end
        end
        data.completedAvailable = type(ids) == "table"
    else
        data.completedAvailable = false
    end

    if type(C_QuestLog.GetNumQuestLogEntries) == "function" and type(C_QuestLog.GetInfo) == "function" then
        for index = 1, C_QuestLog.GetNumQuestLogEntries() do
            local info = C_QuestLog.GetInfo(index)
            if info and not info.isHeader and type(info.questID) == "number" then
                table.insert(data.active, info.questID)
            end
        end
        data.activeAvailable = true
    else
        data.activeAvailable = false
    end

    table.sort(data.completed)
    table.sort(data.active)
end

addon:RegisterEvent("PLAYER_LOGIN")
addon:RegisterEvent("QUEST_LOG_UPDATE")
addon:RegisterEvent("QUEST_TURNED_IN")
addon:RegisterEvent("PLAYER_LOGOUT")
addon:SetScript("OnEvent", function(self, event)
    snapshot()
    if event == "PLAYER_LOGIN" then
        print("|cff00ccffChubbyQuestTracker:|r collecting quest history. Log out to save it.")
    end
end)

SLASH_CHUBBYQUEST1 = "/cqt"
SlashCmdList.CHUBBYQUEST = function()
    snapshot()
    local data = ChubbyQuestTrackerDB or {}
    print("Quest snapshot prepared: " .. tostring(#(data.completed or {})) ..
        " completed, " .. tostring(#(data.active or {})) ..
        " active. Log out normally to save the file.")
end
