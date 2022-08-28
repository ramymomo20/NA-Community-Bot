import discord
import pandas
from discord import Option
from ..config import *
from Statistics.bot_logic import *


@bot.slash_command(name = 'view_rating',description="View Someone's Rating")
async def view_rating(ctx, user: Option(discord.Member, "Enter an @", required = True)):
        
        userid = str(user.id)
        member = await bot.fetch_user(user.id)

        name1 = list(data.Name)
        pos = list(data.Position)
        rate = list(data.Rating)
        ids = list(data.id)
        x = [str(i) for i in ids]


        dict1 = {x[a]:(pos[a],rate[a],name1[a]) for a in range(len(name1))}

        if str(user.id) not in dict1:
            await ctx.respond(ACCOUNT_NOT_FOUND,ephemeral=True)
        else:
            col = discord.Color.greyple()

            if dict1[userid][1] >= 84:
                col = discord.Color.gold()
            if 76 <= dict1[userid][1] <= 83:
                col = discord.Color.dark_gold()
            if 70 <= dict1[userid][1] <= 75:
                col = discord.Color.light_grey()
            if dict1[userid][1] <= 69:
                col = discord.Color.dark_red()

            embed=discord.Embed(title="IOS NA Ratings", url="https://docs.google.com/spreadsheets/d/1awIL1ZtuLw_xFu3-jsv8qlKT8PXCggEYsRdOF9v26b0/edit", description="\n **------------------------** \n", color=col)
            embed.set_author(name=dict1[userid][2], icon_url=member.display_avatar.url)
            embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
            embed.add_field(name="Player", value=dict1[userid][2], inline=True)
            embed.add_field(name="Position", value=dict1[userid][0], inline=True)
            embed.add_field(name="Rating", value=dict1[userid][1], inline=True)
            embed.set_footer(text="Requested by {}".format(ctx.author.name))
            await ctx.respond(embed=embed,ephemeral=True)