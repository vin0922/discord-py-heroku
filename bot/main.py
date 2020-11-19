import os
from discord.ext import commands

bot = commands.Bot(command_prefix=".")
TOKEN = 'Nzc4OTc4ODY1NTk4NDMxMjMy.X7Z2mg.hN-y5_pcKunR1B10gokftNxY_mY'

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)
