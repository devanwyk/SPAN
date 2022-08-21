import sys
from CodingChallenge import *
import pytest

def test_initLeague():
    league = League()
    assert isinstance(league.teams, dict)
    assert isinstance(league.matches, dict)


# def test_mainFileNotFoundError():
    # raise FileNotFoundError after catching
#     with pytest.raises(FileNotFoundError):
#         sys.argv.append('input.txt')
#         main()


def test_addTeam():
    league = League()
    league.addTeam(Team('test'))
    assert league.teams['test'].name == 'test'


def test_removeTeam():
    league = League()
    league.addTeam(Team('test'))
    league.removeTeam(Team('test'))
    assert 'test' not in league.teams


def test_addMatch():
    league = League()
    league.addMatch(Match('teamA', 'teamB', 1, 2))
    assert league.matches['teamA vs teamB'].name == 'teamA vs teamB'


def test_removeMatch():
    league = League()
    league.addMatch(Match('teamA', 'teamB', 1, 2))
    league.removeMatch(Match('teamA', 'teamB', 1, 2))
    assert 'teamA vs teamB' not in league.matches


def test_awardMatchPoints():
    league = League()
    league.addTeam(Team('teamA'))
    league.addTeam(Team('teamB'))
    league.addMatch(Match('teamA', 'teamB', 1, 2))
    league.awardMatchPoints(Match('teamA', 'teamB', 1, 2))
    assert league.teams['teamA'].points == 0
    assert league.teams['teamB'].points == 3
    league.awardMatchPoints(Match('teamA', 'teamB', 2, 1))
    assert league.teams['teamA'].points == 3
    assert league.teams['teamB'].points == 3
    league.awardMatchPoints(Match('teamA', 'teamB', 2, 2))
    assert league.teams['teamA'].points == 4
    assert league.teams['teamB'].points == 4


def test_rankingTable():
    league = League()
    league.addTeam(Team('teamA'))
    league.addTeam(Team('teamB'))
    league.addMatch(Match('teamA', 'teamB', 1, 2))
    league.awardMatchPoints(Match('teamA', 'teamB', 1, 2))
    rankTable = league.rankingTable()
    assert rankTable[3][0].name == 'teamB'
    assert rankTable[0][0].name == 'teamA'
 
    league.awardMatchPoints(Match('teamA', 'teamB', 2, 1))
    rankTable = league.rankingTable()
    assert rankTable[3][1].name == 'teamB'
    assert rankTable[3][0].name == 'teamA'

    league.awardMatchPoints(Match('teamA', 'teamB', 2, 2))
    rankTable = league.rankingTable()
    assert rankTable[4][1].name == 'teamB'
    assert rankTable[4][0].name == 'teamA'
