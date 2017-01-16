import re
from Player import Player

passingPlay = "7-B.Roethlisberger pass short right to 84-A.Brown pushed ob at PIT 47 for 9 yards (54-D.Hightower)."
runningPlay = "(15:00) 34-De.Williams right tackle to PIT 38 for 18 yards (54-D.Hightower)."
interceptionPlay = "(7:09) (No Huddle, Shotgun) 7-B.Roethlisberger pass deep left intended for 88-D.Heyward-Bey INTERCEPTED by 30-D.Harmon at NE 7. 30-D.Harmon ran ob at NE 7 for no gain."

names = re.compile("\d+-[A-z]+\.[A-z]+")        # compiled regex for the first name that appears in the string
passing = re.compile("pass")                    # compiled regex for passing plays NEED TO ADD SOMETHING FOR INCOMPLETE PASSES
run = re.compile("guard | tackle | middle | scrambles")     # compiled regex for running plays
yards = re.compile("for\s(\d+)")                # compiled regex for yardage
interception = re.compile("INTERCEPTED")
fumble = re.compile("FUMBLE")
fumbleLost = re.compile("RECOVERED")            # check to see if fumble is necessary not sure recovered would be used elsewhare
fumbleNotLost = re.compile('recovered')
penalty = re.compile("PENALTY")                 # enforced penalties
sack = re.compile("sacked")
punt = re.compile("punts")
kickOff = re.compile("kicks")
fieldGoalMade = re.compile("field goal is GOOD")
fieldGoalMissed = re.compile("field goal is No Good")
incomplete = re.compile("incomplete")
player_number = re.compile("^(\d+)")
player_name = re.compile("[A-z]+\.[A-z]+")
team_name = re.compile("[A-Z][a-z]+\s[A-z]+(?=\sat)")

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
test_file = open("TestTemp.txt", 'r')

string_to_enterTemp = runningPlay


def play_by_play_parser(string_to_enter):
    """Parses a single line play-by-play text.
    :param string_to_enter: A string for the parser to parse.
    :return:
    """

    if names.search(string_to_enter):
        name_search(string_to_enter)

    if passing.search(string_to_enter):
        passing_play_parse(string_to_enter)

    if run.search(string_to_enter) and not passing.search(string_to_enter):
        # need to work on fumbles but need to work out fumbles recovered vs lost
        running_play_parse(string_to_enter)

    if sack.search(string_to_enter):
        print("sack")


def name_search(string_to_enter):
    matches = names.findall(string_to_enter)
    number_dash_name_parse(matches[0])
    print("name match: %s" % matches)


def passing_play_parse(string_to_enter):
    if interception.search(string_to_enter):
        print("interception")
    elif incomplete.search(string_to_enter):
        print("incomplete")
    else:
        matches = yards.findall(string_to_enter)
        print("passing yds %s" % matches)


def running_play_parse(string_to_enter):
    if fumble.search(string_to_enter):
        if fumbleLost.search(string_to_enter):
            print("fumble lost")
        else:
            print("fumble not lost")
    else:
        matches = yards.findall(string_to_enter)
        print("rushing yds %s" % matches)


def number_dash_name_parse(string_to_parse):
    number = player_number.findall(string_to_parse)
    name = player_name.findall(string_to_parse)
    key_name = name[0].split(".")[1] + number[0]
    if key_name not in player_objects:
        temp = {key_name: Player(name, number, t_name)}
        player_objects.update(temp)


line = test_file.readline()
t_name = "null"
player_objects = {}

while line:
    if team_name.search(line):
        t_name = team_name.findall(line)[0]
    play_by_play_parser(line)
    line = test_file.readline()

for key in player_objects.keys():
    print(key)

test_file.close()

