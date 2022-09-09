import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)

TITLE = "🤖 `NA Community Bot`"
DESCRIPTION = "I manage IOSNA community and I work the ratings system."
HOW_TO_USE = "🤔 How to use me?"
COMMANDS = "⌨️ Available commands"
ADD = "🤝 Copyright (c) 2022 **NA Community Bot**\n*THIS SOFTWARE IS PROVIDED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.*" 
FOOTER_TEXT = "If you require further assistance, directly message: @shaq#6096"
FOOTER_URL = "https://imgur.com/ylgPvo4.jpeg"

USE_MESSAGE = ""
USE_MESSAGE += f"**1**. Get a feel for the bot by using the different commands. This bot uses your 18-digit unique discord id to tie your account with your rating.\n"
USE_MESSAGE += f"**2**. If for any case the bot doesn't work for you, even if you have a rating. I'll have to update your discord id.\n"
USE_MESSAGE += f"**3**. This bot is still a WIP, but we hope to constantly update this to include new commands and added functionality.\n"
USE_MESSAGE += f"**4**. Let me know if there are any bugs or new features you would like to see changed/added!\n"
USE_MESSAGE += f"**5**. Enjoy! Or not.\n"
USE_MESSAGE += "\u200b"

COMMANDS_MESSAGE = ""
COMMANDS_MESSAGE += f"**1**. `/my_rating` to view your rating. However, if you do not have one, or if you created a new discord account, this will not work.\n"
COMMANDS_MESSAGE += f"**2**. `/view_rating @name` to view someone else's rating.\n"
COMMANDS_MESSAGE += f"**3**. `/top_na` to view the top 10 best players in NA.\n"
COMMANDS_MESSAGE += f"**4**. `/ratings (GK, DEF, MID, ATK)` to view the ratings by position using the list of positions in the parentheses.\n"
COMMANDS_MESSAGE += f"**5**. `/8_ball [question]`, ask the bot any question and you shall receive an answer.\n"
COMMANDS_MESSAGE += f"**6**. `/view_top_leagues`, get the league table of any league you like.\n"
COMMANDS_MESSAGE += f"**7**. `/view_top_scorers`, get the top scorer of each team of any league.\n"
COMMANDS_MESSAGE += f""
COMMANDS_MESSAGE += "\u200b"

ADD_MESSAGE = ""
ADD_MESSAGE += ""
ADD_MESSAGE += "\u200b"

#* Success messages ---------------------------------------------------------------------------------------------
DELETED_MSG = "Successfully deleted the messages."
SENT_DM = "DM has been sent!"

# Input errors
YOUR_ACCOUNT_NOT_FOUND = "We do not have your account in your system. Please contact shaq to fix this."
ACCOUNT_NOT_FOUND = "That account is not in the system. Please contact shaq to fix this."
INVALID_PERMISSIONS = "You do not have the permission to do that."
NON_EXISTENT = "That account is invalid."
