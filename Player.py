class Player(object):
    """An individual player in the nfl with a variety of stats available. Players have the following properties:

    Attributes:
            player_id: a unique integer representing the player.
            name: A string representing the players name in the form lastName_firstInitiaal.
            number: An integer with the players current number.
            team: A three character string representing the players current team.
    """
    player_count = 0

    def __init__(self, name, number, team):
        self.player_id = Player.player_count
        self.name = name
        self.number = number
        self.team = team
        self.passing_yards = 0
        self.rushing_yards = 0
        Player.player_count += 1

    def add_passing_yards(self, passing_yards):
        self.passing_yards = self.passing_yards + passing_yards

    def add_rushing_yards(self, rushing_yards):
        self.rushing_yards = self.rushing_yards + rushing_yards

