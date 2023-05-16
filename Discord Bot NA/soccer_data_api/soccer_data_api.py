from soccer_data_api.config import CONF, EURO, UCL, WC
from soccer_data_api.response_types import json_response, int_json_response, cl_json_response, euro_json_response
from soccer_data_api.get_soccer_data import GetData, GetWCData, GetUCLData, GetEUROData


class SoccerDataAPI:
    """
    A class that returns the stats of selected leagues.
    ...
    Methods:
    -------
    <league>: Gets stats (team name, points, matches played, wins, losses, draws, top scorers, goal diff number)
    of selected league
    """
    def __init__(self):
        self.get_data = None

    def world_cup(self):
        self.get_data = GetWCData(WC['wc']['data'])
        response = int_json_response(self.get_data.get_year(),
                                     self.get_data.get_country(), self.get_data.get_champion(),
                                     self.get_data.get_second(), self.get_data.get_top_scorer())
        return response

    def champions_league(self):
        self.get_data = GetUCLData(UCL['cl']['data'])
        response = cl_json_response(self.get_data.get_year(),self.get_data.get_champion(),
                                     self.get_data.get_second(), self.get_data.get_top_scorer())
        return response     

    def europa_league(self):
        self.get_data = GetEUROData(EURO['euro']['data'])
        response = euro_json_response(self.get_data.get_year(),self.get_data.get_champion(),
                                     self.get_data.get_second(), self.get_data.get_top_scorer())
        return response   

    def english_premier(self):
        self.get_data = GetData(CONF['leagues']['english_premier_league'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())

        return response

    def la_liga(self):
        self.get_data = GetData(CONF['leagues']['la_liga'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_position(),
                                 self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())
        
        return response

    def bundesliga(self):
        self.get_data = GetData(CONF['leagues']['bundesliga'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())

        return response

    def serie_a(self):
        self.get_data = GetData(CONF['leagues']['serie_a'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())

        return response

    def ligue_1(self):
        self.get_data = GetData(CONF['leagues']['ligue_1'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())

        return response

    def primeira_liga(self):
        self.get_data = GetData(CONF['leagues']['primeira_liga'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_position(),
                                 self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())
        
        return response
    
    def super_lig(self):
        self.get_data = GetData(CONF['leagues']['super_lig'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_position(),
                                 self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())
        
        return response