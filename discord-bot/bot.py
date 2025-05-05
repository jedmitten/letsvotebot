import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from pyrankvote import RankVote

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def rcv(ctx, *args):
    """Usage: !rcv A,B,C | user1:1,2,3 user2:2,1,3"""
    try:
        options_part, *votes_parts = " ".join(args).split("|")
        options = [opt.strip() for opt in options_part.split(",")]
        ballots = []

        # Parse the votes into a list of lists of rankings
        for vote in votes_parts:
            for v in vote.strip().split():
                rankings = list(map(int, v.split(":")[1].split(",")))
                ballots.append(rankings)

        # Use PyRankVote for instant-runoff voting
        election = RankVote(options, ballots)
        winner = election.get_winner()

        await ctx.send(f"RCV Winner: **{winner}**")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command()
async def poll(ctx, *, arg):
    """Usage: !poll What's your favorite color? | Red, Blue, Green"""
    try:
        question, options_str = map(str.strip, arg.split("|"))
        options = [opt.strip() for opt in options_str.split(",")]
        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

        if len(options) > len(emojis):
            await ctx.send("Too many options (max 10).")
            return

        description = "\n".join(f"{emojis[i]} {opt}" for i, opt in enumerate(options))
        embed = discord.Embed(title=question, description=description, color=0x00ff00)
        msg = await ctx.send(embed=embed)

        for i in range(len(options)):
            await msg.add_reaction(emojis[i])
    except Exception as e:
        await ctx.send(f"Error: {e}")

bot.run(TOKEN)
