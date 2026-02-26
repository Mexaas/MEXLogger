import os
import disnake
from disnake.ext import commands

intents = disnake.Intents().all()
bot = commands.InteractionBot(intents=intents)

@bot.event
async def on_ready():
    # Stable in Windows 11 terminal
    print(
        f"""
        #######################
        #                     #
        # 🚀 {bot.user}   #
        # 🔓 Bot is starting  #
        #                     #
        #######################
        """
    )
bot.load_extensions("Cogs\\Captcha\\")
bot.load_extensions("Events\\VerifyChannel\\")
bot.run(os.getenv("DISCORD_TOKEN"))