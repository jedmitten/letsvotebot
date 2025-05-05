import discord
from discord.ext import commands
from collections import Counter
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def rcv(ctx, *args):
    try:
        options_part, *votes_parts = " ".join(args).split("|")
        options = [opt.strip() for opt in options_part.split(",")]
        ballots = []
        for vote in votes_parts:
            for v in vote.strip().split():
                rankings = list(map(int, v.split(":")[1].split(",")))
                ballots.append(rankings)

        def instant_runoff(options, ballots):
            while True:
                counts = Counter(ballot[0] for ballot in ballots)
                if not counts: return "No winner"
                top = counts.most_common(1)[0]
                if top[1] > len(ballots) / 2:
                    return options[top[0] - 1]
                least = min(counts.values())
                elim = [k for k, v in counts.items() if v == least]
                ballots = [[x for x in ballot if x not in elim] for ballot in ballots]

        result = instant_runoff(options, ballots)
        await ctx.send(f"Winner: {result}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

bot.run(TOKEN)
