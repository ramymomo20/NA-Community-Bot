from bs4 import BeautifulSoup
import requests
from soccer_data_api.config import CONF, EURO, WC
from time import sleep


class GetData:
    """
    A class that gets data/stats from the https://www.sports-reference.com/
    ...
    Attributes
    ----------
    league: str
        Bundesliga has only 18 teams instead of 20. So there is if statement to check if it is a Bundesliga
        to return 18 team stats.

    Methods
    ----------
    get_club_name: Gets name of the team. "[1:]" in "self.array.append(pos.get_text()[1:])" is to get rid of
    the whitespace that method returns.

    get_points: Simply, it's a method that gets the points.

    get_matches_played: Gets the number of matches they played.

    get_wins: Gets the number of wins.

    get_draws: Gets the number of draws.

    get_losses: Gets the number of losses.

    get_goals_for: Gets the number of scored goals.

    get_goals_against: Gets the number of conceded goals.

    get_goal_diff: Gets the difference of get_goals_for and get_goals_against.

    get_top_scorer: Gets the name of the team's top scorer.
    """
    #*******************************************************************************************************
    def __init__(self, league):
        page = requests.get(CONF['url']+league)
        self.soup = BeautifulSoup(page.content, features="html.parser")
        self.league = ""
        self.array = []
        self.pos = []
        self.clubs = []
        self.points = []
        self.games = []
        self.wins = []
        self.draws = []
        self.losses = []
        self.goals_for = []
        self.goals_against = []
        self.goal_diff = []
        self.top_scorer = []
        self.league = league

    def get_position(self):
        raw_response = self.soup.find_all('th', {'data-stat': 'rank'})
        for pos in raw_response:
            self.array.append(pos.get_text())
        self.pos += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.pos[-19:]
        elif self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.pos[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.pos[-16:]
        
        return self.pos[-20:]

    def get_club_name(self):
        raw_response = self.soup.find_all('td', {'class': 'left'})
        for team in raw_response:
            self.array.append(team.get_text()[1:])
        self.clubs += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.clubs[-19:]
        elif self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.clubs[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.clubs[-16:]

        return self.clubs[-20:]

    def get_points(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'points'})
        for points in raw_response:
            self.array.append(points.get_text())
        self.points += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.points[-19:]
        elif self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.points[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.points[-16:]

        return self.points[-20:]

    def get_matches_played(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'games'})
        for games in raw_response:
            self.array.append(games.get_text())
        self.games += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.games[-19:]
        elif self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.games[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.games[-16:]

        return self.games[-20:]

    def get_wins(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'wins'})
        for wins in raw_response:
            self.array.append(wins.get_text())
        self.wins += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.wins[-19:]
        elif self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.wins[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.wins[-16:]

        return self.wins[-20:]

    def get_draws(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'ties'})
        for draws in raw_response:
            self.array.append(draws.get_text())
        self.draws += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.draws[-19:]
        elif self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.draws[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.draws[-16:]

        return self.draws[-20:]

    def get_losses(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'losses'})
        for losses in raw_response:
            self.array.append(losses.get_text())
        self.losses += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.losses[-19:]
        elif self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.losses[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.losses[-16:]

        return self.losses[-20:]

    def get_goals_for(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'goals_for'})
        for gf in raw_response:
            self.array.append(gf.get_text())
        self.goals_for += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.goals_for[-19:]
        elif self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.goals_for[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.goals_for[-16:]

        return self.goals_for[-20:]

    def get_goals_against(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'goals_against'})
        for ga in raw_response:
            self.array.append(ga.get_text())
        self.goals_against += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.goals_against[-19:]
        if self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.goals_against[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.goals_against[-16:]

        return self.goals_against[-20:]

    def get_goal_diff(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'goal_diff'})
        for gd in raw_response:
            self.array.append(gd.get_text())
        self.goal_diff += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.goal_diff[-19:]
        if self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.goal_diff[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.goal_diff[-16:]

        return self.goal_diff[-20:]

    def get_top_scorer(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'top_team_scorers'})
        for top_scorer in raw_response:
            self.array.append(top_scorer.get_text())
        self.top_scorer += self.array

        if self.league == 'comps/26/Super-Lig-Stats':
            return self.top_scorer[-19:]
        elif self.league == "comps/20/Bundesliga-Stats" or self.league == "comps/23/Eredivisie-Stats" or self.league == "comps/32/Primeira-Liga-Stats":
            return self.top_scorer[-18:]
        elif self.league == "comps/30/Russian-Premier-League-Stats":
            return self.top_scorer[-16:]

        return self.top_scorer[-20:]

#*******************************************************************************************************
class GetWCData:
    def __init__(self, wc):
        page = requests.get(WC['url']+wc)
        self.soup = BeautifulSoup(page.content, features="html.parser")
        self.league = ""
        self.array = []
        self.year = []
        self.host = []
        self.champion = []
        self.second = []
        self.top_scorer = []
        self.league = wc

    def get_year(self):
        raw_response = self.soup.find_all('th', {'data-stat': 'year'})
        for years in raw_response:
            self.array.append(years.get_text())
        self.year += self.array

        return self.year[-22:]

    def get_country(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'host_country'})
        for hosts in raw_response:
            self.array.append(hosts.get_text()[:])
        self.host += self.array

        return self.host[-22:]

    def get_champion(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'champ'})
        for champions in raw_response:
            self.array.append(champions.get_text()[3:])
        self.champion += self.array

        return self.champion[-22:]

    def get_second(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'runner_up'})
        for seconds in raw_response:
            self.array.append(seconds.get_text()[3:])
        self.second += self.array

        return self.second[-22:]

    def get_top_scorer(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'top_scorers'})
        for topscorer in raw_response:
            self.array.append(topscorer.get_text())
        self.top_scorer += self.array

        return self.top_scorer[-22:]

#*******************************************************************************************************
class GetUCLData:
    def __init__(self, cl):
        page = requests.get(WC['url']+cl)
        self.soup = BeautifulSoup(page.content, features="html.parser")
        self.league = ""
        self.array = []
        self.year = []
        self.champion = []
        self.second = []
        self.top_scorer = []
        self.league = cl

    def get_year(self):
        raw_response = self.soup.find_all('th', {'data-stat': 'year_id'})
        for years in raw_response:
            self.array.append(years.get_text())
        self.year += self.array

        return self.year[-32:]

    def get_champion(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'champ'})
        for champions in raw_response:
            self.array.append(champions.get_text()[3:])
        self.champion += self.array

        return self.champion[-32:]

    def get_second(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'runner_up'})
        for seconds in raw_response:
            self.array.append(seconds.get_text()[3:])
        self.second += self.array

        return self.second[-32:]

    def get_top_scorer(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'top_scorers'})
        for topscorer in raw_response:
            self.array.append(topscorer.get_text())
        self.top_scorer += self.array

        return self.top_scorer[-32:]

#*******************************************************************************************************
class GetEUROData:
    def __init__(self, euro):
        page = requests.get(EURO['url']+euro)
        self.soup = BeautifulSoup(page.content, features="html.parser")
        self.league = ""
        self.array = []
        self.year = []
        self.champion = []
        self.second = []
        self.top_scorer = []
        self.league = euro

    def get_year(self):
        raw_response = self.soup.find_all('th', {'data-stat': 'year_id'})
        for years in raw_response:
            self.array.append(years.get_text())
        self.year += self.array

        return self.year[-32:]

    def get_champion(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'champ'})
        for champions in raw_response:
            self.array.append(champions.get_text()[3:])
        self.champion += self.array

        return self.champion[-32:]

    def get_second(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'runner_up'})
        for seconds in raw_response:
            self.array.append(seconds.get_text()[3:])
        self.second += self.array

        return self.second[-32:]

    def get_top_scorer(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'top_scorers'})
        for topscorer in raw_response:
            self.array.append(topscorer.get_text())
        self.top_scorer += self.array

        return self.top_scorer[-32:]
