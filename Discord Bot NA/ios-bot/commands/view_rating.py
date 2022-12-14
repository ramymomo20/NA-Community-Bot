import discord
from discord import Option
from ..config import *
from bot_logic import *


@bot.slash_command(name = 'view_rating',description="View Someone's Rating")
async def view_rating(ctx, user: Option(discord.Member, "Enter an @", required = True)):
        
        userid = str(user.id)
        member = await bot.fetch_user(user.id)

        name1 = list(data.Name)
        pos = list(data.Position)
        rate = list(data.Rating)
        ids = list(data.ID)
        improved = list(data.Improved)
        x = [str(i) for i in ids]


        dict1 = {x[a]:(pos[a],rate[a],name1[a], improved[a]) for a in range(len(name1))}

        if str(user.id) not in dict1:
            await ctx.respond(ACCOUNT_NOT_FOUND,ephemeral=True)
        else:
            col = discord.Color.greyple()

            if dict1[userid][3] == 100:
                tex = 'You are a new addition!'
            else:
                if dict1[userid][3] < 0:
                    num = int(dict1[userid][3])
                    tex = f"```diff\n-{num*-1} from last rating.```"
                if dict1[userid][3] == 0:
                    tex = "```fix\n0 from last rating.```"
                if dict1[userid][3] > 0:
                    num = int(dict1[userid][3])
                    tex = f"```diff\n+{num} from last rating.```"

            if dict1[userid][1] >= 84:
                col = discord.Color.gold()
            if 76 <= dict1[userid][1] <= 83:
                col = discord.Color.dark_gold()
            if 69 <= dict1[userid][1] <= 75:
                col = discord.Color.light_grey()
            if dict1[userid][1] <= 68:
                col = discord.Color.dark_red()

            embed=discord.Embed(title="IOS NA Ratings", url="https://docs.google.com/spreadsheets/d/1ZUWs-zHYjIpJvVPSTofodg8FF29_zP28Mmk5j9ZtynU/edit?usp=sharing", description="\n **------------------------** \n", color=col)
            embed.set_author(name=dict1[userid][2], icon_url=member.display_avatar.url)
            embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
            embed.add_field(name="Player", value=dict1[userid][2], inline=True)
            embed.add_field(name="Position", value=dict1[userid][0], inline=True)
            embed.add_field(name="Rating", value=dict1[userid][1], inline=True)
            embed.add_field(name="Change", value=tex,inline=False)
            embed.set_footer(text="Requested by {}".format(ctx.author.name))
            await ctx.respond(embed=embed)