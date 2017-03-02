import re
from Player import Player


names_regex = re.compile("\d+-[A-z]+\.[A-z]+")        # compiled regex for the first name that appears in the string
passing_regex = re.compile("pass")                    # compiled regex for passing plays NEED TO ADD SOMETHING FOR INCOMPLETE PASSES
run_regex = re.compile("guard | tackle | middle | scrambles | right end | left end")     # compiled regex for running plays
yards_regex = re.compile("for\s(-*\d+)")                # compiled regex for yardage
interception_regex = re.compile("INTERCEPTED")
fumble_regex = re.compile("FUMBLE")
fumble_lost_regex = re.compile("RECOVERED")            # check to see if fumble is necessary not sure recovered would be used elsewhare
fumble_not_lost_regex = re.compile('recovered')
penalty_regex = re.compile("PENALTY")                 # enforced penalties
sack_regex = re.compile("sacked")
punt_regex = re.compile("punts")
kick_off_regex = re.compile("kicks")
field_goal_made_regex = re.compile("field goal is GOOD")
field_goal_missed_regex = re.compile("field goal is No Good")
incomplete_regex = re.compile("incomplete")
player_number_regex = re.compile("^(\d+)")
player_name_regex = re.compile("[A-z]+\.[A-z]+")
team_name_regex = re.compile("[A-Z][a-z]+\s[A-z]+(?=\sat)")


team_abbreviations = {'Arizona Cardinals': 'ARI',
                      'Atlanta Falcons': 'ATL',
                      'Baltimore Ravens': 'BAL',
                      'Buffalo Bills': 'BUF',
                      'Carolina Panthers': 'CAR',
                      'Chicago Bears': 'CHI',
                      'Cincinnati Bengals': 'CIN',
                      'Cleveland Browns': 'CLE',
                      'Dallas Cowboys': 'DAL',
                      'Denver Broncos': 'DEN',
                      'Detroit Lions': 'DET',
                      'Green Bay Packers': 'GBP',
                      'Houston Texans': 'HOU',
                      'Indianapolis Colts': 'IND',
                      'Jacksonville Jaguars': 'JAX',
                      'Kansas City Chiefs': 'KCC',
                      'Los Angeles Rams': 'LAR',
                      'Los Angeles Chargers': 'LAC',
                      'Miami Dolphins': 'MIA',
                      'Minnesota Vikings': 'MIN',
                      'New England Patriots': 'NEP',
                      'New Orleans Saints': 'NOS',
                      'New York Giants': 'NYG',
                      'New York Jets': 'NYJ',
                      'Oakland Raiders': 'OAK',
                      'Philadelphia Eagles': 'PHI',
                      'Pittsburgh Eagles': 'PIT',
                      'San Diego Chargers': 'SDC',
                      'Seattle Seahawks': 'SEA',
                      'St. Louis Rams': 'STL',
                      'Tampa Bay Buccaneers': 'TBB',
                      'Tennessee Titans': 'TEN',
                      'Washington Redskins': 'WAS'}


player_objects = {}
#     offensive_team_name = "null"


def play_by_play_parser(string_to_enter, off_team_name):
    """Parses a single line play-by-play text.
    :param string_to_enter: A String for the parser to parse.
    :param off_team_name: A String. The current offensive team
    :return:
    """

    if names_regex.search(string_to_enter):
        name_search(string_to_enter, off_team_name)

    if passing_regex.search(string_to_enter):
        # if penalty_regex.search(string_to_enter):
        #     print('PENALTY')
        # else:
        #     passing_play_parse(string_to_enter, off_team_name)
        passing_play_parse(string_to_enter, off_team_name)

    if run_regex.search(string_to_enter) and not passing_regex.search(string_to_enter):
        # need to work on fumbles, but need to work out fumbles recovered vs lost
        running_play_parse(string_to_enter, off_team_name)

    if sack_regex.search(string_to_enter):
        print("sack")


def name_search(string_to_enter, off_team_name):
    matches = names_regex.findall(string_to_enter)
    number_dash_name_parse(matches[0], off_team_name)
    print("name match: %s" % matches)
    return matches


def passing_play_parse(string_to_enter, off_team_name):
    """
    Parses a running play.
    :param string_to_enter: String that consists of a single [passing] play from the game log.
    :param off_team_name: String that consists of the team currently on offense for the play.
    :return:
    """
    names_to_parse = name_search(string_to_enter, off_team_name)
    temp_list = []
    for i in range(len(names_to_parse)):
        temp_list.append(names_to_parse[i])
    # if interception_regex.search(string_to_enter) and not penalty_regex.search(string_to_enter):
    if interception_regex.search(string_to_enter):
        print("interception!!!!!!!")
        temp_list = []
        for i in range(4):
            temp_list.append(number_dash_name_parse(names_to_parse[i], off_team_name))
        player_objects.get(temp_list[0]).add_passing_attempt()
        player_objects.get(temp_list[0]).add_interception()
    elif incomplete_regex.search(string_to_enter) and not penalty_regex.search(string_to_enter):
        print("incomplete")
        temp_list = []
        for i in range(2):
            temp_list.append(number_dash_name_parse(names_to_parse[i], off_team_name))
        player_objects.get(temp_list[0]).add_passing_attempt()
    elif not penalty_regex.search(string_to_enter):
        matches = yards_regex.findall(string_to_enter)
        matches.append('0')
        print("passing yds %s" % matches)
        temp_list = []
        for i in range(2):
            temp_list.append(number_dash_name_parse(names_to_parse[i], off_team_name))
        player_objects.get(temp_list[0]).add_passing_yards(int(matches[0]))
        player_objects.get(temp_list[0]).add_passing_attempt()
        player_objects.get(temp_list[1]).add_reception_yards(int(matches[0]))
        player_objects.get(temp_list[1]).add_reception()


def running_play_parse(string_to_enter, off_team_name):
    """
    Parses a running play.
    :param string_to_enter: String that consists of a single [running] play from the game log.
    :param off_team_name: String that consists of the team currently on offense for the play.
    :return:
    """
    if fumble_regex.search(string_to_enter):
        if fumble_lost_regex.search(string_to_enter):
            print("fumble lost")
        else:
            print("fumble not lost")
    else:
        matches = yards_regex.findall(string_to_enter)
        matches.append('0')
        print("rushing yds %s" % matches)
        names_to_parse = name_search(string_to_enter, off_team_name)
        temp_list = []
        for i in range(1):
            temp_list.append(number_dash_name_parse(names_to_parse[i], off_team_name))
        print('RUSHING YARDS: ')
        print((matches[0]))
        print(temp_list)
        player_objects.get(temp_list[0]).add_rushing_yards(int(matches[0]))


# going to have to work on getting the team name(offensive_team_name) for each player correct.
def number_dash_name_parse(string_to_parse, off_team_name):
    number = player_number_regex.findall(string_to_parse)
    name = player_name_regex.findall(string_to_parse)
    key_name = name[0].split(".")[1] + number[0]
    if key_name not in player_objects:
        temp = {key_name: Player(name, number, off_team_name)}
        player_objects.update(temp)
    return key_name


def run_entire_game_log():
    """Runs an entire game log, eventually it should take a :param of filename but usingt test_file for now
    """
    test_file = open("TestTemp.txt", 'r')
    line = test_file.readline()
    offensive_team_name = "null"
    while line:
        if team_name_regex.search(line):
            offensive_team_name = team_name_regex.findall(line)[0]
        play_by_play_parser(line, offensive_team_name)
        line = test_file.readline()

    for key in player_objects.keys():
        print(key)

    print(len(player_objects))
    print(player_objects.get('Murray28').rushing_yards)
    print(player_objects.get('Fuller15').receptions)
    print(player_objects.get('Fuller15').receiving_yards)

    test_file.close()
    return player_objects


# run_entire_game_log()
