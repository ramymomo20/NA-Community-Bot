import discord, asyncio
from soccer_logic import *
from ..config import bot
import collections
collections.Callable = collections.abc.Callable

class Select1(discord.ui.View):
    @discord.ui.select(placeholder = "Select a league: ",min_values = 1,max_values = 1,options = [
            discord.SelectOption(
                label="English Premier League",
                description="Pick this if you want the English League",
                emoji = "🇬🇧"
            ),
            discord.SelectOption(
                label="La Liga",
                description="Pick this if you want the Spanish League!",
                emoji = "🇪🇸"
            ),
            discord.SelectOption(
                label="Ligue 1",
                description="Pick this if you want the French League!",
                emoji = "🇫🇷"
            ),
            discord.SelectOption(
                label="Bundesliga",
                description="Pick this if you want the German League!",
                emoji = '🇩🇪'
            ),
            discord.SelectOption(
                label="Serie A",
                description="Pick this if you want the Italian League!",
                emoji = '🇮🇹'
            ),
            discord.SelectOption(
                label="Eredivisie",
                description="Pick this if you want the Dutch League!",
                emoji = "🇳🇱"
            ),
            discord.SelectOption(
                label="Russian Premier League",
                description="Pick this if you want the Russian League!",
                emoji = "🇷🇺"
            ),
            discord.SelectOption(
                label="Primeira Liga",
                description="Pick this if you want the Portuguese League!",
                emoji = "🇵🇹"
            ),
            discord.SelectOption(
                label="Super Lig",
                description="Pick this if you want the Turkish League!",
                emoji = "🇹🇷"
            )
        ]
    )
    
    async def select_callback(self, select, interaction):
        if select.values[0] == "English Premier League":
            select.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("```{}```".format(Start.gettable(1)),ephemeral=False)
            
        elif select.values[0] == "La Liga":
            select.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("```{}```".format(Start.gettable(2)),ephemeral=False)

        elif select.values[0] == "Ligue 1":
            select.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("```{}```".format(Start.gettable(3)),ephemeral=False)

        elif select.values[0] == "Bundesliga":
            select.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("```{}```".format(Start.gettable(4)),ephemeral=False)

        elif select.values[0] == "Serie A":
            select.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("```{}```".format(Start.gettable(5)),ephemeral=False)

        elif select.values[0] == "Eredivisie":
            select.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("```{}```".format(Start.gettable(6)),ephemeral=False)

        elif select.values[0] == "Russian Premier League":
            select.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("```{}```".format(Start.gettable(7)),ephemeral=False)

        elif select.values[0] == "Primeira Liga":
            select.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("```{}```".format(Start.gettable(8)),ephemeral=False)

        elif select.values[0] == "Super Lig":
            select.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("```{}```".format(Start.gettable(9)),ephemeral=False)

@bot.slash_command(name = 'view_league_table',description="View the league tables")
async def league_table(ctx):
    await ctx.respond("Choose the league you want to view!", view=Select1(timeout=False),ephemeral=True)