import sys
from collections import defaultdict

class League():
    
    def __init__(self):
        """Constructor to instantiate teams and matches dictionaries"""
        self.teams = dict()
        self.matches = dict()


    def addTeam(self, team):
        """Adds a team to the league"""
        if team.name not in self.teams:
            self.teams[team.name] = team


    def removeTeam(self, team):
        """Removes a team from the league if required"""
        if team.name in self.teams:
            del self.teams[team.name]


    def addMatch(self, match):
        """Adds a match to the league"""
        if match.name not in self.matches:
            self.matches[match.name] = match

    def removeMatch(self, match):
        """Removes a match from the league if required"""
        if match.name in self.matches:
            del self.matches[match.name]


    def awardMatchPoints(self, match):
        """Awards points to each team based on the rules of the league"""

        if match.teamAscore == match.teamBscore: # draw\tie
            self.teams[match.teamAname].points += 1
            self.teams[match.teamBname].points += 1

        elif match.teamAscore > match.teamBscore: # teamA wins
            self.teams[match.teamAname].points += 3

        elif match.teamAscore < match.teamBscore: # teamB wins
            self.teams[match.teamBname].points += 3


    def rankingTable(self):
        """Builds a ranking table using a dictionary where the keys are
        the points scored to enable building a list of teams with same 
        scores."""

        rankTable = defaultdict(list)

        # first sort the teams with most points first
        pointsDict = sorted(self.teams.values(), key=lambda item: item.points, reverse=True)
        
        # build the ranking table using points as key and compile list of teams with same points
        for rank, team in enumerate(pointsDict):
            rankTable[team.points].append(team)
                            
        # print the ranking table
        for rank, teamlist in enumerate(rankTable):
            rankTable[teamlist].sort(key=lambda item: item.name)
            for team in rankTable[teamlist]:
            #for team in sorted(rankTable[teamlist], key=lambda item: item.name):
                pts = 'pts'
                if team.points == 1:
                    pts = 'pt'
                print('%d. %s, %d %s' %(rank+1, team.name,team.points, pts))
        
        return rankTable
 

class Team():
    """The Team class stores information about a team
    such as team name and points awarded in the league"""
    
    def __init__(self, name):
        self.name = name
        self.points = 0


class Match():
    """The Match class stores information about a match or game
    such as teams played and their scores"""

    def __init__(self, teamAname, teamBname, teamAscore, teamBscore):
        self.name = teamAname + ' vs ' + teamBname
        self.teamAname = teamAname
        self.teamBname = teamBname
        self.teamAscore = int(teamAscore)
        self.teamBscore = int(teamBscore)


def main() -> int:
    """The main method or entry point for the command line program"""

    if len(sys.argv) < 2:
        print('\nUsage e.g: python CodingChallenge.py "inputfile.txt" \n')
        return 0

    inFile = sys.argv[1]

    try:
        with open(inFile,'r') as f:

            superLeague = League()
            
            for line in f:
                #split match line\record into teams and scores
                matchText = line.split(',') 
                
                # for each team in match split out name and score
                teamAText = matchText[0].strip().split()
                teamBText = matchText[1].strip().split()

                teamA = Team(' '.join(teamAText[:-1])) 
                superLeague.addTeam(teamA)

                teamB = Team(' '.join(teamBText[:-1]))
                superLeague.addTeam(teamB)

                match = Match(teamA.name, teamB.name, teamAText[-1], teamBText[-1])
                superLeague.addMatch(match)
                superLeague.awardMatchPoints(match)
                
            # Print the ranking table
            ranks = superLeague.rankingTable()

    except FileNotFoundError as fer:
        print(fer)
        #raise fer #for testing purposes

    return 0


# Enable module to be run from command line as well as to be imported
if __name__ == '__main__':
    sys.exit(main())

