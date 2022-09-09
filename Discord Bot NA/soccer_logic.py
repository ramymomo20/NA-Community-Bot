from soccer_data_api import SoccerDataAPI
import functools
from prettytable import PrettyTable
soccer_data = SoccerDataAPI()

def table(focused_league):
    myTable = PrettyTable(["Position", "Team", "Points", "Matches Played", "Wins", "Draws", "Losses", "Goal Difference"])
    myTable.border = False
    for data in focused_league[:]:
        myTable.add_row([data['pos'], data['team'], data['points'], data['matches_played'], data['wins'], data['draws'], data['losses'], data['goal_diff']])
    return ((myTable))

def top_scorer(focused_league):
    myTable = PrettyTable(['Team', 'Top Scorers'])
    myTable.border = False
    for data in focused_league[:]:
        myTable.add_row([data['team'], data['top_scorer']])

    lst = []
    lst2 = []
    for data in focused_league[:]:
        lst.append(data['top_scorer'][-2:])
        lst2.append(data['top_scorer'])
    return (myTable)

class Start:
    def gettable(index):
        if index == 1:
            return table(soccer_data.english_premier())
        if index == 2:
            return table(soccer_data.la_liga())
        if index == 3:
            return table(soccer_data.ligue_1())
        if index == 4:
            return table(soccer_data.bundesliga())
        if index == 5:
            return table(soccer_data.serie_a())
        if index == 6:
            return table(soccer_data.eredivisie())
        if index == 7:
            return table(soccer_data.russian_premier())
        if index == 8:
            return table(soccer_data.primeira_liga())
        if index == 9:
            return table(soccer_data.super_lig())       

class Scorers:
    def getScorers(index):
        if index == 1:
            return top_scorer(soccer_data.english_premier())
        if index == 2:
            return top_scorer(soccer_data.la_liga())
        if index == 3:
            return top_scorer(soccer_data.ligue_1())
        if index == 4:
            return top_scorer(soccer_data.bundesliga())
        if index == 5:
            return top_scorer(soccer_data.serie_a())
        if index == 6:
            return top_scorer(soccer_data.eredivisie())
        if index == 7:
           return top_scorer(soccer_data.russian_premier()) 
        if index == 8:
            return top_scorer(soccer_data.primeira_liga())
        if index == 9:
            return top_scorer(soccer_data.super_lig()) 