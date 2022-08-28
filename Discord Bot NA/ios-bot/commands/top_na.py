import discord
from ..config import *
from Statistics.bot_logic import *

@bot.slash_command(name = 'top_na',description="View the 10 Best Players in NA")
async def top_na(ctx):
        
        embed=discord.Embed(title="Top 10 NA Players", url="https://docs.google.com/spreadsheets/d/1awIL1ZtuLw_xFu3-jsv8qlKT8PXCggEYsRdOF9v26b0/edit", description="\n **------------------------** \n", color=discord.Color.og_blurple())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
        embed.add_field(name="Player", value='\n'.join(map(str, highest.highestnames())), inline=True)
        embed.add_field(name="Position", value='\n'.join(map(str, highest.highestpos())), inline=True)
        embed.add_field(name="Rating", value='\n'.join(map(str, highest.highestratings())), inline=True)
        embed.add_field(name="The Best Player is{}".format(highest.highestnames()[0].replace('1.',"")), value='**------------------------**', inline=False)
        embed.set_footer(text="Requested by {}".format(ctx.author.name))
        await ctx.respond(embed=embed,ephemeral=True)