import unittest
from PlayByPlayParser import run_entire_game_log

player_stats = run_entire_game_log()


class KnownRushingYards(unittest.TestCase):
    known_rushing_yard_values = (('Miller26', 73),
                                 ('Murray28', 39),
                                 ('Grimes41', 30),
                                 ('Washington33', 16)
                                 )

    def test_compare_rushing_yards_to_known(self):
        """get_rushing_yards should give known result with a known input"""
        for name, yards in self.known_rushing_yard_values:
            result = player_stats.get(name).rushing_yards
            self.assertEqual(yards, result)


class KnownReceivingYards(unittest.TestCase):
    known_receiving_yards = (('Holmes18', 50),
                             ('Hopkins10', 67),
                             ('Fuller15', 37),
                             ('Crabtree15', 33))

    def test_compare_receiving_yards_to_known(self):
        """get_receiving yards should give known result with a known input"""
        for name, yards in self.known_receiving_yards:
            result = player_stats.get(name).receiving_yards
            self.assertEqual(yards, result)


class KnownNumberOfReceptions(unittest.TestCase):
    known_number_of_receptions = (('Holmes18', 4),
                                  ('Hopkins10', 5),
                                  ('Fuller15', 4),
                                  ('Crabtree15', 2))

    def test_compare_number_of_receptions(self):
        """compares a known number of receptions with a known input"""
        for name, receptions in self.known_number_of_receptions:
            result = player_stats.get(name).receptions
            self.assertEqual(receptions, result)


if __name__ == '__main__':
    unittest.main()
