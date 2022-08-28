import discord
import pandas
from Statistics.bot_logic import *
from discord import Option
from ..config import *

@bot.slash_command(name = 'ratings',description='Enter either: (GK, DEF, MID, or ATK)')
async def ratings(ctx, position: Option(str, "Enter a Position (GK, DEF, MID, ATK)", required=True)):

        name = list(data.Name)
        pos = list(data.Position)
        rate = list(data.Rating)

        x = [[name[i],pos[i],rate[i]] for i in range(len(rate))]

        attackers = [newlst for sublist in x for newlst in [sublist] if sublist[1] == "ATK"]
        attack_names, attack_rating = [item[0] for item in attackers],[item[2] for item in attackers]

        midfielders = [newlst for sublist in x for newlst in [sublist] if sublist[1] == "MID"]
        mid_names, mid_rating = [item[0] for item in midfielders],[item[2] for item in midfielders]

        defender = [newlst for sublist in x for newlst in [sublist] if sublist[1] == "DEF"]
        def_names, def_rating = [item[0] for item in defender],[item[2] for item in defender]

        goalkeeper = [newlst for sublist in x for newlst in [sublist] if sublist[1] == "GK"]
        gk_names, gk_rating = [item[0] for item in goalkeeper],[item[2] for item in goalkeeper]


        if position == 'GK' or position == 'gk':
            embed=discord.Embed(title="Current Goalkeeper Ratings", url="https://docs.google.com/spreadsheets/d/1awIL1ZtuLw_xFu3-jsv8qlKT8PXCggEYsRdOF9v26b0/edit", description="\n **------------------------------------------** \n", color=discord.Color.random())
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
            embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
            embed.add_field(name="Players ", value='\n'.join(map(str, gk_names)), inline=True)
            embed.add_field(name="Ratings ", value='\n'.join(map(str, gk_rating)), inline=True)
            embed.set_footer(text="Requested by {}".format(ctx.author.name))    
            await ctx.respond(embed=embed,ephemeral=True)

        elif position == 'DEF' or position == 'def':
            embed=discord.Embed(title="Current Defender Ratings", url="https://docs.google.com/spreadsheets/d/1awIL1ZtuLw_xFu3-jsv8qlKT8PXCggEYsRdOF9v26b0/edit", description="\n **------------------------------------------** \n", color=discord.Color.random())
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
            embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
            embed.add_field(name="Players ", value='\n'.join(map(str, def_names)), inline=True)
            embed.add_field(name="Ratings ", value='\n'.join(map(str, def_rating)), inline=True)
            embed.set_footer(text="Requested by {}".format(ctx.author.name))    
            await ctx.respond(embed=embed,ephemeral=True)
        
        elif position == 'MID' or position == 'mid':
            embed=discord.Embed(title="Current Midfielder Ratings", url="https://docs.google.com/spreadsheets/d/1awIL1ZtuLw_xFu3-jsv8qlKT8PXCggEYsRdOF9v26b0/edit", description="\n **------------------------------------------** \n", color=discord.Color.random())
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
            embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
            embed.add_field(name="Players ", value='\n'.join(map(str, mid_names)), inline=True)
            embed.add_field(name="Ratings ", value='\n'.join(map(str, mid_rating)), inline=True)
            embed.set_footer(text="Requested by {}".format(ctx.author.name))    
            await ctx.respond(embed=embed,ephemeral=True)

        elif position == 'ATK' or position == 'atk':
            embed=discord.Embed(title="Current Attacker Ratings", url="https://docs.google.com/spreadsheets/d/1awIL1ZtuLw_xFu3-jsv8qlKT8PXCggEYsRdOF9v26b0/edit", description="\n **------------------------------------------** \n", color=discord.Color.random())
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
            embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
            embed.add_field(name="Players ", value='\n'.join(map(str, attack_names)), inline=True)
            embed.add_field(name="Ratings ", value='\n'.join(map(str, attack_rating)), inline=True)
            embed.set_footer(text="Requested by {}".format(ctx.author.name))    
            await ctx.respond(embed=embed,ephemeral=True)
        else:
            await ctx.respond("That position is invalid.",ephemeral=True)