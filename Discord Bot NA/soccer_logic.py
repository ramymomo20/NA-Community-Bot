from soccer_data_api import SoccerDataAPI
import functools
from prettytable import PrettyTable
soccer_data = SoccerDataAPI()

class FunctionHolder:        
    def table(focused_league):
        myTable = PrettyTable(["Position", "Team", "Points", "Matches Played", "Wins", "Draws", "Losses", "Goal Difference"])
        myTable.border = False
        for data in focused_league[:]:
            myTable.add_row([data['pos'], data['team'], data['points'], data['matches_played'], data['wins'], data['draws'], data['losses'], data['goal_diff']])

        myTable.align["Position"] = "c"
        myTable.align["Team"] = "c"
        myTable.align["Points"] = "c"
        myTable.align["Matches Played"] = "c"
        myTable.align["Wins"] = "c"
        myTable.align["Draws"] = "c"
        myTable.align["Losses"] = "c"
        myTable.align["Goal Difference"] = "c"

        # Limit the maximum width of the columns in the table
        myTable.max_width["Team"] = 30
        return (myTable)
class FunctionHolder:        
    def table(focused_league):
        myTable = PrettyTable(["Position", "Team", "Points", "Matches Played", "Wins", "Draws", "Losses", "Goal Difference"])
        myTable.border = False
        for data in focused_league[:]:
            myTable.add_row([data['pos'], data['team'], data['points'], data['matches_played'], data['wins'], data['draws'], data['losses'], data['goal_diff']])

        myTable.align["Position"] = "c"
        myTable.align["Team"] = "c"
        myTable.align["Points"] = "c"
        myTable.align["Matches Played"] = "c"
        myTable.align["Wins"] = "c"
        myTable.align["Draws"] = "c"
        myTable.align["Losses"] = "c"
        myTable.align["Goal Difference"] = "c"

        # Limit the maximum width of the columns in the table
        myTable.max_width["Team"] = 30
        return (myTable)

    def top_scorer(focused_league):
        myTable = PrettyTable(['Team', 'Top Scorers'])
        myTable.border = False
        for data in focused_league[:]:
            myTable.add_row([data['team'], data['top_scorer']])
    def top_scorer(focused_league):
        myTable = PrettyTable(['Team', 'Top Scorers'])
        myTable.border = False
        for data in focused_league[:]:
            myTable.add_row([data['team'], data['top_scorer']])

        # Sort the rows in the table by the 'Team' column in alphabetical order
        myTable.sortby = "Team"

        myTable.align["Team"] = "c"
        myTable.align["Top Scorers"] = "c"

        # Limit the maximum width of the columns in the table
        myTable.max_width["Team"] = len(myTable.rows)
        myTable.max_width["Top Scorers"] = 2 * len(myTable.rows)
        return (myTable)


    def WCtable(focused_league):
        myTable = PrettyTable(["Year", 'Champion', "Runners-Up", 'Hosts'])
        myTable.border = False
        for data in focused_league[:-8]:
            myTable.add_row([data['year'], data['champion'], data['second'], data['host']])

        # Align the text in the 'Year', 'Champion', and 'Runners-Up' columns to the right, and the text in the 'Hosts' column to the left
        myTable.align["Year"] = "c"
        myTable.align["Champion"] = "c"
        myTable.align["Runners-Up"] = "c"
        myTable.align["Hosts"] = "c"
        return (myTable)


    def CLtable(focused_league):
        myTable = PrettyTable(["Season", 'Champion', "Runners-Up", 'Top Scorer'])
        myTable.border = False
        
        for data in focused_league[:-10]:
            myTable.add_row([data['season'], data['champion'], data['second'], data['top_scorer']])
            
        myTable.align["Season"] = "c"
        myTable.align["Champion"] = "c"
        myTable.align["Runners-Up"] = "c"
        myTable.align["Top Scorer"] = "c"

        # Set a maximum width for the columns in the table
        myTable.max_width = 40
        
        # Iterate over the rows in the table
        for row in myTable.rows:
            # Extract the last two characters of the first four-character substring of the year
            year1 = row[0][:4][-2:]

            # Extract the last two characters of the second four-character substring of the year
            year2 = row[0][-4:][-2:]

            two_year_period = year1 + "-" + year2
            row[0] = two_year_period
        
        return (myTable)

    def UELtable(focused_league):
        myTable = PrettyTable(["Season", 'Champion', "Runners-Up", 'Top Scorer'])
        myTable.border = False
        for data in focused_league[:-10]:
            myTable.add_row([data['season'], data['champion'], data['second'], data['top_scorer']])
            
        myTable.align["Season"] = "c"
        myTable.align["Champion"] = "c"
        myTable.align["Runners-Up"] = "c"
        myTable.align["Top Scorer"] = "c"

        myTable.max_width = 40
        
        # Iterate over the rows in the table
        for row in myTable.rows:
            # Extract the last two characters of the first four-character substring of the year
            year1 = row[0][:4][-2:]

            # Extract the last two characters of the second four-character substring of the year
            year2 = row[0][-4:][-2:]

            two_year_period = year1 + "-" + year2
            row[0] = two_year_period
        return (myTable)
        # Sort the rows in the table by the 'Team' column in alphabetical order
        myTable.sortby = "Team"

        myTable.align["Team"] = "c"
        myTable.align["Top Scorers"] = "c"

        # Limit the maximum width of the columns in the table
        myTable.max_width["Team"] = len(myTable.rows)
        myTable.max_width["Top Scorers"] = 2 * len(myTable.rows)
        return (myTable)


    def WCtable(focused_league):
        myTable = PrettyTable(["Year", 'Champion', "Runners-Up", 'Hosts'])
        myTable.border = False
        for data in focused_league[:-8]:
            myTable.add_row([data['year'], data['champion'], data['second'], data['host']])

        # Align the text in the 'Year', 'Champion', and 'Runners-Up' columns to the right, and the text in the 'Hosts' column to the left
        myTable.align["Year"] = "c"
        myTable.align["Champion"] = "c"
        myTable.align["Runners-Up"] = "c"
        myTable.align["Hosts"] = "c"
        return (myTable)


    def CLtable(focused_league):
        myTable = PrettyTable(["Season", 'Champion', "Runners-Up", 'Top Scorer'])
        myTable.border = False
        
        for data in focused_league[:-10]:
            myTable.add_row([data['season'], data['champion'], data['second'], data['top_scorer']])
            
        myTable.align["Season"] = "c"
        myTable.align["Champion"] = "c"
        myTable.align["Runners-Up"] = "c"
        myTable.align["Top Scorer"] = "c"

        # Set a maximum width for the columns in the table
        myTable.max_width = 40
        
        # Iterate over the rows in the table
        for row in myTable.rows:
            # Extract the last two characters of the first four-character substring of the year
            year1 = row[0][:4][-2:]

            # Extract the last two characters of the second four-character substring of the year
            year2 = row[0][-4:][-2:]

            two_year_period = year1 + "-" + year2
            row[0] = two_year_period
        
        return (myTable)

    def UELtable(focused_league):
        myTable = PrettyTable(["Season", 'Champion', "Runners-Up", 'Top Scorer'])
        myTable.border = False
        for data in focused_league[:-10]:
            myTable.add_row([data['season'], data['champion'], data['second'], data['top_scorer']])
            
        myTable.align["Season"] = "c"
        myTable.align["Champion"] = "c"
        myTable.align["Runners-Up"] = "c"
        myTable.align["Top Scorer"] = "c"

        myTable.max_width = 40
        
        # Iterate over the rows in the table
        for row in myTable.rows:
            # Extract the last two characters of the first four-character substring of the year
            year1 = row[0][:4][-2:]

            # Extract the last two characters of the second four-character substring of the year
            year2 = row[0][-4:][-2:]

            two_year_period = year1 + "-" + year2
            row[0] = two_year_period
        return (myTable)

class Getters:
class Getters:
    def gettable(index):
        options_dictionary = {
            1: FunctionHolder.table(soccer_data.english_premier()),
            2: FunctionHolder.table(soccer_data.la_liga()),
            3: FunctionHolder.table(soccer_data.ligue_1()),
            4: FunctionHolder.table(soccer_data.bundesliga()),
            5: FunctionHolder.table(soccer_data.serie_a()),
            6: FunctionHolder.table(soccer_data.eredivisie()),
            7: FunctionHolder.table(soccer_data.russian_premier()),
            8: FunctionHolder.table(soccer_data.primeira_liga()),
            9: FunctionHolder.table(soccer_data.super_lig())} 
               
        return options_dictionary[index]

        options_dictionary = {
            1: FunctionHolder.table(soccer_data.english_premier()),
            2: FunctionHolder.table(soccer_data.la_liga()),
            3: FunctionHolder.table(soccer_data.ligue_1()),
            4: FunctionHolder.table(soccer_data.bundesliga()),
            5: FunctionHolder.table(soccer_data.serie_a()),
            6: FunctionHolder.table(soccer_data.eredivisie()),
            7: FunctionHolder.table(soccer_data.russian_premier()),
            8: FunctionHolder.table(soccer_data.primeira_liga()),
            9: FunctionHolder.table(soccer_data.super_lig())} 
               
        return options_dictionary[index]

    def getScorers(index):
        options_dictionary = {
            1: FunctionHolder.top_scorer(soccer_data.english_premier()),
            2: FunctionHolder.top_scorer(soccer_data.la_liga()),
            3: FunctionHolder.top_scorer(soccer_data.ligue_1()),
            4: FunctionHolder.top_scorer(soccer_data.bundesliga()),
            5: FunctionHolder.top_scorer(soccer_data.serie_a()),
            6: FunctionHolder.top_scorer(soccer_data.eredivisie()),
            7: FunctionHolder.top_scorer(soccer_data.russian_premier()),
            8: FunctionHolder.top_scorer(soccer_data.primeira_liga()),
            9: FunctionHolder.top_scorer(soccer_data.super_lig())} 
               
        return options_dictionary[index]
    
    def getTournamentHistory(index):
        options_dictionary = {
            1: FunctionHolder.WCtable(soccer_data.world_cup()),
            2: FunctionHolder.CLtable(soccer_data.champions_league()),
            3: FunctionHolder.UELtable(soccer_data.europa_league())}
        return options_dictionary[index]
    
print(Getters.gettable(2))
print(Getters.getScorers(1))