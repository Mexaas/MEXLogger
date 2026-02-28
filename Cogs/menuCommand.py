import disnake
from disnake.ext import commands

class menuCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    emoji = [1477235042475315240] # main emoji

    @commands.slash_command(description="Навигационная команда", guild_ids=[1466509350100013226])
    async def menu(self, body: disnake.ApplicationCommandInteraction):
        await body.response.send_message(
            f"""
            # {self.bot.get_emoji(self.emoji[0])} Навигация
            - /remove_thread ` Удаляет ветку, если вы владелец `
            """,
            ephemeral=True
        )
        return
    
def setup(bot):
    bot.add_cog(menuCommand(bot))