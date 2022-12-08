from ..config import *

@bot.slash_command(name = '8_ball',description="Ask the Bot for your Fate.")
async def the8ball(ctx, question):

    responses = ['It is certain.',
                 'It is decidedly so.', 
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Do not count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.',
                 'Hell No',
                 'Hell Yeah',
                 "I don't see it",
                 "Don't think so.",
                 "Your questions aren't worth answering.",
                 "Yes, 100%",
                 "Ask someone else.",
                 'Not in a million years.',
                 "Find God.",
                 "You are in luck",
                 "NEVER.",
                 "For sure, definitely.",
                 "You are onto something.",
                 "Close, but no cigar.",
                 "You are on the right path.",
                 "You only speak facts.",
                 "You should be arrested for misinformation.",
                 "Nah, will not happen,"
                 "Honestly, do not even bother.",
                 "Get some help.",
                 'Nope.',
                 'Positive',
                 'From my point of view, yes',
                 'Convinced.',
                 'Chances High',
                 'No.',
                 'Negative.',
                 'Nah, sorry.',
                 'Perhaps.',
                 'Probably.',
                 "Maybe",
                 "I'm to lazy to predict.",
                 "I am tired. *proceeds with sleeping*",
                 "Sure, why not.",
                 "How can you even say that...",
                 "Don't speak of this again.",
                 "I couldn't think of anything dumber than that.",
                 "You are a genius."]

    rep = random.choice(responses)

    embed = discord.Embed(title='Receive Your Fate',color=discord.Color.random())
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
    embed.set_thumbnail(url="https://imgur.com/ylgPvo4.jpeg")
    embed.add_field(name='Your Question: ', value=f'{question}', inline=True)
    embed.add_field(name='The Bot Says: ',value=f'{rep}', inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.respond(embed=embed)