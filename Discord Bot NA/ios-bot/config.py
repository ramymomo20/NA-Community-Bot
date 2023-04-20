import discord
from discord.ext import commands
from discord import Option
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = discord.Bot(intents=intents)

link = 'https://docs.google.com/spreadsheets/d/1BP-nsM2rS200hLALOrOyGZv2IFkAMLzPAGB-NojbRtA/edit?usp=sharing'

TITLE = "🤖 `NA Community Bot`"
DESCRIPTION = "I manage the IOSNA community and I work the ratings system."
HOW_TO_USE = "🤔 How to use me?"
COMMANDS = "⌨️ Available commands"
ADD = "🤝 Copyright (c) 2023 **NA Community Bot**\n*THIS SOFTWARE IS PROVIDED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.*" 
FOOTER_TEXT = "If you require further assistance, directly message: @shaq#6096"
FOOTER_URL = "https://imgur.com/ylgPvo4.jpeg"

COMMANDS_MESSAGE = ""
COMMANDS_MESSAGE += f"**1**. `/my_rating` to view your rating. However, if you do not have one, or if you created a new discord account, this will not work.\n"
COMMANDS_MESSAGE += f"**2**. `/view_rating @name` to view someone else's rating.\n"
COMMANDS_MESSAGE += f"**3**. `/top_na` to view the top 10 best players in NA.\n"
COMMANDS_MESSAGE += f"**4**. `/ratings (GK, DEF, MID, ATK)` to view the ratings by position using the list of positions in the parentheses.\n"
COMMANDS_MESSAGE += f"**5**. `/8_ball [question]`, ask the bot any question and you shall receive an answer.\n"
COMMANDS_MESSAGE += f"**6**. `/view_league_table`, view the league table of the top leagues in Europe.\n"
COMMANDS_MESSAGE += f"**5**. `/top_scorers`, view the top scorers of the top leagues.\n"
COMMANDS_MESSAGE += f"**5**. `/view_tournament`, view tournaments like the World Cup, CL, and EL.\n"
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
