Having a community of over 3000 members on the North America IOSoccer Discord is an achievement that is noteworthy. But, occasionally with each passing event or game that goes on, there is a notable feeling of "emptiness" in the discord. Nothing to record stats, review performances, and tier people's skill level. So here we are: The NA Community Bot. 

A bot that creates a rating system from the https://iosoccer.com/player-list that output people's ratings and outputs them in a colored-tier system based on FIFA's card system. Not only that, a viewing of the top 10 best, each rating by position, as well as a system to view other's ratings individually. Not just that, but a few community moderating commands to keep the community secure. With passing updates, I've added integrations with openai API for better responses to user's questions. This API is from the CHAT GPT 3.5 Turbo model. As well as integration from the jokeapi for jokes too. However, these jokes are not appropriate, so use at your own risk to avoid offensive responses.

## Usage

The way this bot works is as follows:

You basically have a few slash commands that you input in any given channel. However, you must be a registered player. To be registered, you must have played at least 10 matches with us in a given month. Some kind of activity to show you are there. Once that has been satisfied, we take the stats of the performances in those matches and compile a rating that reflects that. This rating will be linked to your discord ID and is now apart of our database. With each passing month, a new ratings list will come out.

Here's the list of commands:

| Command                       | Action                                                                                                     |
| :---------------------------- | :--------------------------------------------------------------------------------------------------------- |
| `/ help`                      | `ios-bot` will private message you a list of commands and their usage (i.e., basically everything in here) |
| `/ prompt [question]`         | ask the `ios-bot` anything and you shall receive a GPT 3.5 answer.                                         |
| `/ 8_ball [question]`         | ask the `ios-bot` anything too and you shall receive a GPT-8-ball-like answer                              |
| `/ joke`                      | (USE AT YOUR OWN RISK) the `ios-bot` will give you a joke.                                                 |
| `/ my_rating`                 | View your rating with your main position.                                                                  |
| `/ top_na`                    | View the top-10 best players with their rating and position.                                               |
| `/ view_rating @member`       | View the rating of a given @member                                                                         |
| `/ ratings(GK, DEF, MID, ATK)`| View the ratings by a specified position.                                                                  |
| `/ view_league_table`         | View the league table of any league IRL.                                                                   |
| `/ view_top_scorers`          | View the top scorers of any league IRL with each team.                                                     |
| `/ view_tournaments`          | View the winners of the World Cup, CL, and UL.                                                             |
| `/ motm [url]`                | receive the MOTM of the match given the url.                                                               |
| `/ clear [number]` *ADMIN*    | Deletes a specified number of previous messages from chat.                                                 |
| `/ get_id @member` *ADMIN*    | Receives the unique 18 digit ID of a user.                                                                 |
