import re

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
fumbleNotLost = re.compile("recovered")
penalty = re.compile("PENALTY")                 # enforced penalties
sack = re.compile("sacked")
punt = re.compile("punts")
kickOff = re.compile("kicks")
fieldGoalMade = re.compile("field goal is GOOD")
fieldGoalMissed = re.compile("field goal is No Good")
incomplete = re.compile("incomplete")


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
    print("name match: %s" % matches)


def passing_play_parse(string_to_enter):
    if interception.search(string_to_enter):
        print("interception")
    elif incomplete.search(string_to_enter):
        print("incompletion")
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

line = test_file.readline()
while line:
    play_by_play_parser(line)
    line = test_file.readline()

test_file.close()