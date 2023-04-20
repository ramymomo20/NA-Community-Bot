import discord
from soccer_logic import *
from ..config import bot
import collections
collections.Callable = collections.abc.Callable

class Select1(discord.ui.View):
    options = [
        discord.SelectOption(
            label="World Cup",
            description="Pick this if you want the World Cup!",
            emoji = "🌎"
        ),
        discord.SelectOption(
            label="UEFA Champions League",
            description="Pick this if you want the Champions League",
            emoji = "🇪🇺"
        ),
        discord.SelectOption(
            label="UEFA Europa League",
            description="Pick this if you want the Europa League!",
            emoji = "🇪🇺"
        )
    ]

    @discord.ui.select(placeholder = "Select a Tournament: ", min_values = 1, max_values = 1, options = options)

    async def select_callback(self, select, interaction):
        select.disabled = True
        await interaction.response.edit_message(view=self)

        if select.values[0] == "World Cup":
            await interaction.followup.send(f"```{Getters.getTournamentHistory(1)}```", ephemeral=False)
        elif select.values[0] == "UEFA Champions League":
            await interaction.followup.send(f"```{Getters.getTournamentHistory(2)}```", ephemeral=False)
        elif select.values[0] == "UEFA Europa League":
            await interaction.followup.send(f"```{Getters.getTournamentHistory(3)}```", ephemeral=False)


@bot.slash_command(name = 'view_tournament',description="View the CL, EURO, and World Cups")
async def tournament(ctx):
    await ctx.respond("Choose the tournament you want to view!", view=Select1(timeout=False),ephemeral=True)