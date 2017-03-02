import unittest
from PlayByPlayParser import run_entire_game_log

player_stats = run_entire_game_log()


class KnownRushingYards(unittest.TestCase):
    known_rushing_yard_values = (('Miller26', 73),
                                 ('Murray28', 39),
                                 ('Grimes41', 30),
                                 ('Washington33', 16)
                                 )
    known_fumbles = (('Osweiler17', 1),
                     ('Miller26', 0))

    def test_compare_rushing_yards_to_known(self):
        """get_rushing_yards should give known result with a known input"""
        for name, yards in self.known_rushing_yard_values:
            result = player_stats.get(name).rushing_yards
            self.assertEqual(yards, result)

    def test_compare_fumbles_to_known(self):
        """compares number of fumbles with a known input"""
        for name, fumbles in self.known_fumbles:
            result = player_stats.get(name).fumbles
            self.assertEqual(fumbles, result)

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


class KnownReceivingStats(unittest.TestCase):
    known_number_of_receptions = (('Holmes18', 4),
                                  ('Hopkins10', 5),
                                  ('Fuller15', 4),
                                  ('Crabtree15', 2))

    def test_compare_number_of_receptions(self):
        """compares a known number of receptions with a known input"""
        for name, receptions in self.known_number_of_receptions:
            result = player_stats.get(name).receptions
            self.assertEqual(receptions, result)


class KnownPassingStats(unittest.TestCase):
    known_passing_yards = (('Osweiler17', 168),
                           ('Cook8', 161))
    known_passing_attempts = (('Osweiler17', 25),
                              ('Cook8', 45))
    known_interceptions_thrown = (('Osweiler17', 0),
                                  ('Cook8', 3))

    known_completions = (('Osweiler17', 14),
                         ('Cook8', 18))

    def test_compare_number_of_passing_yards(self):
        """"compares a known number for passing yards with a known input"""
        for name, passing_yards in self.known_passing_yards:
            result = player_stats.get(name).passing_yards
            self.assertEqual(passing_yards, result)

    def test_compare_number_of_passing_attempts(self):
        """compares a known number of passing attempts given a known input"""
        for name, passing_attempts in self.known_passing_attempts:
            result = player_stats.get(name).passing_attempts
            self.assertEqual(passing_attempts, result)

    def test_compare_interception_numbers(self):
        """compares known number of interceptions given a known input"""
        for name, interceptions in self.known_interceptions_thrown:
            result = player_stats.get(name).interceptions
            self.assertEqual(interceptions, result)

    def test_compare_completion_numbers(self):
        """compares known number of completions given a known input"""
        for name, completions in self.known_completions:
            result = player_stats.get(name).completions
            self.assertEqual(completions, result)


if __name__ == '__main__':
    unittest.main()
