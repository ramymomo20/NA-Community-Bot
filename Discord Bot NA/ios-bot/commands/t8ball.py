from ..config import *
from chatgpt.app import ball

@bot.slash_command(name = '8_ball',description="Ask the Bot for your Fate.")
async def the8ball(ctx, question):
    if question == '':
        return ctx.respond('You input nothing...', ephemeral=True)
    embed = discord.Embed(title='Receive Your Fate',color=discord.Color.random())
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
    embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
    embed.add_field(name='Your Question: ', value=f'{question}', inline=True)
    embed.add_field(name='The Bot Says: ',value=f'{ball(question)}', inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.respond(embed=embed)