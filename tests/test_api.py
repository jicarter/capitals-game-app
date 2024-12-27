import unittest
from src.api import fetch_schedule, fetch_next_game

class TestAPI(unittest.TestCase):

    def test_fetch_schedule(self):
        schedule = fetch_schedule()
        self.assertIsInstance(schedule, list)

    def test_fetch_next_game(self):
        next_game = fetch_next_game()
        if next_game:  # Only test if games are available
            self.assertIn("date", next_game)
            self.assertIn("home_team", next_game)
            self.assertIn("away_team", next_game)

if __name__ == "__main__":
    unittest.main()
