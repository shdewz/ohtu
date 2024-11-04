import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_right_player(self):
        self.assertAlmostEqual(self.stats.search("Semenko").goals, 4)

    def test_search_not_found_returns_none(self):
        self.assertAlmostEqual(self.stats.search("AAA"), None)

    def test_team_returns_correct_length_list(self):
        self.assertAlmostEqual(len(self.stats.team("EDM")), 3)
    
    def test_top_first_place_correct_points(self):
        self.assertAlmostEqual(self.stats.top(3, SortBy.POINTS)[0].points, 124)

    def test_top_first_place_correct_goals(self):
        self.assertAlmostEqual(self.stats.top(3, SortBy.GOALS)[0].goals, 45)

    def test_top_first_place_correct_assists(self):
        self.assertAlmostEqual(self.stats.top(3, SortBy.ASSISTS)[0].assists, 89)
