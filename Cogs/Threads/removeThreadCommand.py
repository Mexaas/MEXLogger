import disnake
from disnake.ext import commands
import asyncio
from Database.database import db

class removeThreadCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    emoji = [1477235020740690023, 1477235040084557848] # main emoji

    @commands.slash_command(description="Удаляет ветку, если вы являетесь её владельцем, и находитесь в ней", guild_ids=[1466509350100013226])
    async def remove_thread(self, body: disnake.ApplicationCommandInteraction):
        current_channel = body.channel
        if isinstance(current_channel, disnake.Thread):
            cursor = await db.execute(
                """
                SELECT owner_id, message_id, channel_id FROM threads WHERE thread_id = ?
                """,
                (current_channel.id,)
            )
            row = await cursor.fetchone()
            if not row:
                await body.response.send_message("# :x: Такой ветки нет в системе", ephemeral=True); 
                return
            
            if row[0] != body.author.id:
                await body.response.send_message(
                    """
                    # :x: Ошибка
                    - Вы ` не создатель ` данной ветки!
                    """,
                    ephemeral=True
                )
                return
            channel = body.guild.get_channel(row[2])
            await body.response.send_message(
                f"""
                # {self.bot.get_emoji(self.emoji[0])} Удаление ветки
                - Удаляем ` ветку `, подождите немного..
                """,
                ephemeral=True
            )
            await asyncio.sleep(2)
            await channel.get_partial_message(row[1]).delete()

            await current_channel.delete(
                reason=f"Удалено через команду, пользователем {body.author.display_name}"
            )
            await db.execute(
                """
                DELETE FROM threads WHERE thread_id = ?
                """,
                (current_channel.id,)
            )
            await db.commit()

            return
        else:
            await body.response.send_message(
                """
                # :x: Ошибка
                - Вы ` не находитесь ` ни в какой ветке!
                """,
                ephemeral=True
            )
            return
    
def setup(bot):
    bot.add_cog(removeThreadCommand(bot))