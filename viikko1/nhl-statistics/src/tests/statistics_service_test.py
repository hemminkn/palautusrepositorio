import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_palauttaa_pelaajan(self):
        player = self.stats.search("Semenko")

        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_palauttaa_none_jos_ei_pelaajaa(self):
        player = self.stats.search("Immonen")

        self.assertEqual(player, None)

    def test_palauttaa_tiimin(self):
        players = self.stats.team("EDM")

        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_palauttaa_tyhjan_listan_jos_ei_tiimia(self):
        players = self.stats.team("PPP")

        self.assertEqual(players, [])

    def test_parhaat_pelaajat_ilman_ohjeita(self):
        top_list = self.stats.top(3)

        self.assertEqual(top_list[0].name, "Gretzky")
        self.assertEqual(top_list[1].name, "Lemieux")
        self.assertEqual(top_list[2].name, "Yzerman")

    def test_parhaat_pelaajat_pisteiden_perusteella(self):
        top_list = self.stats.top(3, SortBy.POINTS)

        self.assertEqual(top_list[0].name, "Gretzky")
        self.assertEqual(top_list[1].name, "Lemieux")
        self.assertEqual(top_list[2].name, "Yzerman")

    def test_parhaat_pelaajat_maalien_perusteella(self):
        top_list = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(top_list[0].name, "Lemieux")
        self.assertEqual(top_list[1].name, "Yzerman")
        self.assertEqual(top_list[2].name, "Kurri")

    def test_parhaat_pelaajat_syottojen_perusteella(self):
        top_list = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(top_list[0].name, "Gretzky")
        self.assertEqual(top_list[1].name, "Yzerman")
        self.assertEqual(top_list[2].name, "Lemieux")



