import os
import disnake
from disnake.ext import commands
from Database import database

intents = disnake.Intents().all()
bot = commands.InteractionBot(
    intents=intents,
    activity=disnake.CustomActivity(name="🌸 /menu")
)

@bot.event
async def on_ready():
    await database.init()

    bot.load_extensions("Cogs/Captcha/")
    bot.load_extensions("Cogs/Threads/")
    bot.load_extensions("Cogs/")
    bot.load_extensions("Events/VerifyChannel/")
    bot.load_extensions("Events/SuggestionsChannel/")
    bot.load_extensions("Events/GeneralDataEvent/")
    await database.db.execute("PRAGMA journal_mode=WAL;")
    await database.db.commit()
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

bot.run(os.getenv("DISCORD_TOKEN"))