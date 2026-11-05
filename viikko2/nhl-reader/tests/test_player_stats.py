import unittest
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from index import PlayerStats


class StubPlayerReader:
    def __init__(self, players):
        self.players = players


class PlayerStatsTests(unittest.TestCase):
    def setUp(self):
        self.players = [
            SimpleNamespace(
                name="Player One",
                nationality="FIN",
                team="DAL",
                goals=20,
                assists=30,
            ),
            SimpleNamespace(
                name="Player Two",
                nationality="FIN",
                team="BOS",
                goals=35,
                assists=10,
            ),
            SimpleNamespace(
                name="Player Three",
                nationality="USA",
                team="DAL",
                goals=25,
                assists=20,
            ),
        ]
        self.stats = PlayerStats(StubPlayerReader(self.players))

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in result],
            ["Player One", "Player Two"],
        )

    def test_top_goal_scorers_sorts_by_goals_and_limits_results(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in result],
            ["Player Two", "Player Three"],
        )

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("DAL")

        self.assertEqual(
            [player.name for player in result],
            ["Player One", "Player Three"],
        )

    def test_queries_return_empty_list_when_there_are_no_matches(self):
        self.assertEqual(self.stats.top_scorers_by_nationality("SWE"), [])
        self.assertEqual(self.stats.top_scorers_by_team("NYR"), [])


if __name__ == "__main__":
    unittest.main()
