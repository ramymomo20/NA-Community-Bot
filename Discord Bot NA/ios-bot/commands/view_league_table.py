import discord
from soccer_logic import *
from ..config import bot
import collections
collections.Callable = collections.abc.Callable

LEAGUE_OPTIONS = {
    "English Premier League": 1,
    "La Liga": 2,
    "Ligue 1": 3,
    "Bundesliga": 4,
    "Serie A": 5,
    "Eredivisie": 6,
    "Russian Premier League": 7,
    "Primeira Liga": 8,
    "Super Lig": 9,
}

class Select1(discord.ui.View):
    @discord.ui.select(placeholder="Select a league: ", min_values=1, max_values=1, options=[
            discord.SelectOption(
                label="English Premier League",
                description="Pick this if you want the English League",
                emoji="🇬🇧",
            ),
            discord.SelectOption(
                label="La Liga",
                description="Pick this if you want the Spanish League!",
                emoji="🇪🇸",
            ),
            discord.SelectOption(
                label="Ligue 1",
                description="Pick this if you want the French League!",
                emoji="🇫🇷",
            ),
            discord.SelectOption(
                label="Bundesliga",
                description="Pick this if you want the German League!",
                emoji="🇩🇪",
            ),
            discord.SelectOption(
                label="Serie A",
                description="Pick this if you want the Italian League!",
                emoji="🇮🇹",
            ),
            discord.SelectOption(
                label="Eredivisie",
                description="Pick this if you want the Dutch League!",
                emoji="🇳🇱",
            ),
            discord.SelectOption(
                label="Russian Premier League",
                description="Pick this if you want the Russian League!",
                emoji="🇷🇺",
            ),
            discord.SelectOption(
                label="Primeira Liga",
                description="Pick this if you want the Portuguese League!",
                emoji="🇵🇹",
            ),
            discord.SelectOption(
                label="Super Lig",
                description="Pick this if you want the Turkish League!",
                emoji="🇹🇷",
            ),
        ],
    )
    
    async def select_callback(self, select, interaction):
        select.disabled = True
        await interaction.response.edit_message(view=self)

        # Get the league id using the league name
        league_id = LEAGUE_OPTIONS.get(select.values[0])

        # If the league name is valid, send the league table
        if league_id:
            await interaction.followup.send(f"```{Getters.gettable(league_id)}```", ephemeral=False)

@bot.slash_command(name = 'view_league_table',description="View the league tables")
async def league_table(ctx):
    await ctx.respond("Choose the league you want to view!", view=Select1(timeout=False),ephemeral=True)