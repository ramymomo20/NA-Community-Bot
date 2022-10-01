import discord
from ..config import *
from bot_logic import *

@bot.slash_command(name = 'top_na',description="View the 10 Best Players in NA")
async def top_na(ctx):
        
        embed=discord.Embed(title="Top 10 NA Players", url="https://docs.google.com/spreadsheets/d/11F0008W7lM07f_0byxyvFVHtGNJ3Y5Q0uDMDLxUtAow/edit?usp=sharing", description="\n **------------------------** \n", color=discord.Color.og_blurple())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
        embed.add_field(name="Player", value='\n'.join(map(str, highest(data1).highestnames())), inline=True)
        embed.add_field(name="Position", value='\n'.join(map(str, highest(data1).highestpos())), inline=True)
        embed.add_field(name="Rating", value='\n'.join(map(str, highest(data1).highestratings())), inline=True)
        embed.add_field(name="The Best Player is{}".format(highest(data1).highestnames()[0].replace('1.',"")), value='**------------------------**', inline=False)
        embed.set_footer(text="Requested by {}".format(ctx.author.name))
        await ctx.respond(embed=embed)