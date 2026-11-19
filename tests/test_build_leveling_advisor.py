import unittest
from build_leveling_advisor import build

C = {"name": "Chubby Cheekz", "level": 41, "race": "Troll",
     "className": "Warrior", "items": [], "fetchedAt": 1795116998457}
Q = {"character": "Chubby Cheekz", "completedAvailable": True,
     "activeAvailable": True, "completed": [1, 2], "active": [196, 99999],
     "updatedAt": 1795118061}
CAT = {"quests": [{"id": 196, "name": "Raptor Mastery",
                   "zone": "Stranglethorn Vale", "type": "field",
                   "note": "Jungle Stalkers", "source": "https://example.com"}]}

class AdvisorTests(unittest.TestCase):
    def test_current_and_unknown(self):
        report = build(C, Q, CAT)
        self.assertIn("level 41", report)
        self.assertIn("Raptor Mastery", report)
        self.assertIn("Unmapped active quest IDs: 99999", report)

    def test_updates(self):
        report = build(dict(C, level=42),
                       dict(Q, completed=[1, 2, 99999], active=[196]), CAT)
        self.assertIn("level 42", report)
        self.assertNotIn("#99999", report)

    def test_rejects_incomplete_or_inconsistent(self):
        for quests in (dict(Q, completedAvailable=False),
                       dict(Q, active=[1]),
                       dict(Q, active=[196, 196])):
            with self.assertRaises(ValueError):
                build(C, quests, CAT)

if __name__ == "__main__":
    unittest.main()
