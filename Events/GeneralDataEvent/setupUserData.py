from disnake.ext import commands
import disnake
from Database.database import db

class defaultUserDataSetup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    autosetup_channels = [1476554222874132491, 1476961225127628992, 1477014878102356028]
    emojis = [1477235040084557848]
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return
        if message.channel.id in self.autosetup_channels:
            async with db.execute(
                "SELECT join_value FROM users WHERE user_id = ?",
                (message.author.id,)
            ) as cursor:
                row = await cursor.fetchone()
                if row and row[0] == 0:
                    return
                if not row or row[0] == 1:
                    

                    await db.execute(
                        """
                        INSERT INTO users (user_id, join_value)
                        VALUES (?, 0)
                        ON CONFLICT(user_id)
                        DO UPDATE SET join_value = 0
                        """,
                        (message.author.id,)
                    )
                    await db.commit()
                    
                    embed = disnake.Embed(
                        title="",
                        description=f"""
                                    # {self.bot.get_emoji(self.emojis[0])} Привет, {message.author.mention}!\n
                                    - Добро пожаловать на ` {message.guild.name} `
                                    > Похоже ты здесь впервые 🙂
                                    > используй ` /menu ` для полной навигации
                                    """,
                        color=0x846eff
                    )
                    embed.set_image(url="https://cdn.discordapp.com/attachments/1473895873074303229/1477338431091638574/5e39e8f9-9d93-4058-b603-226334216f9a.png?ex=69a46621&is=69a314a1&hm=07fc0b5eda344f5b60696dba2695e6f7cc0b3128603e4b53640bef9264a605f1&")
                    embed.set_footer(text="© 2026. Все права защищены")
                    await message.channel.send(delete_after=120, embed=embed)

                    return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot: return
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, join_value) VALUES (?, ?)",
            (member.id, 1)
        )
        await db.commit()
        return

def setup(bot):
    bot.add_cog(defaultUserDataSetup(bot))