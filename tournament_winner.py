"""
Tournament Winner
There’s an algorithms tournament taking place in which teams of programmers compete against each other to solve
algorithmic problems as fast as possible. Teams compete in a round-robin, where each team faces off against all other
teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home
team, while the other is the away team. In each competition there’s always one winner and one loser; there are no ties.
A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives
the most amount of points.
Given an array of pairs representing that have competed against each other and an array containing the results of each
competition, write a function that returns the winner of the tournament. The input arrays are named competitions and
results, respectively. The competition arrays has elements in the form of [homeTeam, awayTeam], where each team is as
string at most of 30 characters representing the name of the team. The results array contains information about
the winner of each corresponding competition won and a 0 means that the away team won.
It’s guaranteed that exactly one team will win the tournament and that each team will compete against all other
teams exactly once. It’s also guaranteed that the tournament will always have at least two teams.


"""

from icecream import ic

competitions_01 = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results_01 = [0, 0, 1]

competitions_02 = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
]
results_02 = [0, 1, 1]


def tournament_winner_00(c, r):
    k = [x for x in set([y for x in c for y in x])]
    teams = dict.fromkeys(k, 0)
    _results = [x * 3 for x in r]
    for i in range(len(r)):
        home_team = c[i][0]
        away_team = c[i][1]
        if r[i] == 0:
            teams[away_team] += 3
        elif r[i] == 1:
            teams[home_team] += 3
    return max(teams, key=teams.get)


def tournament_winner_01(c, r):
    teams = {}
    for i in range(len(r)):
        if r[i] == 0:
            teams[c[i][0]]


if __name__ == '__main__':
    competitions = competitions_02
    results = results_02
    print(tournament_winner_00(competitions, results))
