import unittest
from import_quests import parse, ids

EXAMPLE = """
ChubbyQuestTrackerDB = {
    ["character"] = "Chubby Cheekz",
    ["realm"] = "Normal",
    ["updatedAt"] = 1795116998,
    ["completedAvailable"] = true,
    ["activeAvailable"] = true,
    ["completed"] = {
        [1] = 10,
        [2] = 20,
        [3] = 10,
    },
    ["active"] = {
        [1] = 30,
        [2] = 40,
    },
}
"""

class QuestImportTests(unittest.TestCase):
    def test_parse(self):
        data = parse(EXAMPLE)
        self.assertEqual(data["character"], "Chubby Cheekz")
        self.assertEqual(data["completed"], [10, 20])
        self.assertEqual(data["active"], [30, 40])

    def test_empty(self):
        self.assertEqual(ids('["active"] = {}', "active"), [])

    def test_wrong_source(self):
        with self.assertRaises(ValueError):
            parse(EXAMPLE.replace("ChubbyQuestTrackerDB =", "OtherAddon ="))

if __name__ == "__main__":
    unittest.main()
