import os
import disnake
from disnake.ext import commands

intents = disnake.Intents().all()
bot = commands.InteractionBot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is starting")

bot.load_extension("Cogs.Captcha.captchaCommand")
bot.run(os.getenv("DISCORD_TOKEN"))