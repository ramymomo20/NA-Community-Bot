import discord
from soccer_logic import *
from ..config import bot
import collections
collections.Callable = collections.abc.Callable

class Select1(discord.ui.View):
    # Use a list comprehension to create a list of SelectOption objects
    options = [
        discord.SelectOption(
            label=league,
            description=f"Pick this if you want the {league}!",
            emoji=emoji,
        )
        for league, emoji in [
            ("English Premier League", "🇬🇧"),
            ("La Liga", "🇪🇸"),
            ("Ligue 1", "🇫🇷"),
            ("Bundesliga", "🇩🇪"),
            ("Serie A", "🇮🇹"),
            ("Eredivisie", "🇳🇱"),
            ("Russian Premier League", "🇷🇺"),
            ("Primeira Liga", "🇵🇹"),
            ("Super Lig", "🇹🇷"),
        ]
    ]

    @discord.ui.select(placeholder="Select a league: ", min_values=1, max_values=1, options=options)

    async def select_callback(self, select, interaction):
        select.disabled = True
        await interaction.response.edit_message(view=self)

        # Use a dictionary to map option labels to league IDs
        leagues = {
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

        league_id = leagues.get(select.values[0])
        if league_id:
            await interaction.followup.send(f"```{Getters.getScorers(league_id)}```", ephemeral=False)

@bot.slash_command(name = 'view_top_scorers',description="View top scorers in a league")
async def top_scorers(ctx):
    await ctx.respond("Choose the league you want to view!", view=Select1(timeout=False),ephemeral=True)