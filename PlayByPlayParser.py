import re

passingPlay = "7-B.Roethlisberger pass short right to 84-A.Brown pushed ob at PIT 47 for 9 yards (54-D.Hightower)."
runningPlay = "(15:00) 34-De.Williams right tackle to PIT 38 for 18 yards (54-D.Hightower)."
interceptionPlay = "(7:09) (No Huddle, Shotgun) 7-B.Roethlisberger pass deep left intended for 88-D.Heyward-Bey INTERCEPTED by 30-D.Harmon at NE 7. 30-D.Harmon ran ob at NE 7 for no gain."

names = re.compile("\d+-[A-z]+\.[A-z]+")        # compiled regex for the first name that appears in the string
passing = re.compile("pass")                    # compiled regex for passing plays NEED TO ADD SOMETHING FOR INCOMPLETE PASSES
run = re.compile("guard | tackle | middle ")     # compiled regex for running plays
yards = re.compile("for\s(\d+)")                # compiled regex for yardage
interception = re.compile("INTERCEPTED")
fumble = re.compile("FUMBLE")
fumbleLost = re.compile("RECOVERED")            # check to see if fuble is necessary not sure recovered would be used elsewhare
fumbleNotLost = re.compile("recovered")
penalty = re.compile("PENALTY")                 # enforeced penalties
sack = re.compile("sacked")
punt = re.compile("punts")
kickOff = re.compile("kicks")
fieldGoalMade = re.compile("field goal is GOOD")
fieldGoalMissed = re.compile("field goal is No Good")
incomplete = re.compile("incomplete")



testFile = open("TestTemp.txt", 'r')

stringToEnterTemp = runningPlay

def playByPlayParser(stringToEnter):
    # finding all the names in the string
    if names.search(stringToEnter):
        matches = names.findall(stringToEnter)
        print("match: %s" % (matches))
    # determing if it is a passing play, if so return the passing yards
    if passing.search(stringToEnter):
        # need to check if there is an intercetption using ifElse
        if interception.search(stringToEnter):
            print("interception")
        elif incomplete.search(stringToEnter):
            print ("incompletion")
        else:
            matches = yards.findall(stringToEnter)
            print("passing yds %s" % (matches))

    # determing if it is a running play, if so return the rushing yards
    if run.search(stringToEnter) and not passing.search(stringToEnter):
        # need to work on fumbles but need to work out fumbles recovered vs lost
        if fumble.search(stringToEnter):
            if fumbleLost.search(stringToEnter):
                print("fumble lost")
            else:
                print("fumble not lost")
        else:
            matches = yards.findall(stringToEnter)
            print("rushing yds %s" % (matches))

    #checking for a sack
    if sack.search(stringToEnter):
        print("sack")


line = testFile.readline()
while line:
    playByPlayParser(line)
    line = testFile.readline()

testFile.close()
#print (testFile.readline())
#print (testFile.readline())