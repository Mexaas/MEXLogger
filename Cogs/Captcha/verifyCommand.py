import disnake
from disnake.ext import commands

class VerificationCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        description="Верифицирует пользователя автоматически",
        default_member_permissions=disnake.Permissions(
            administrator=True
        ),
    )
    async def verify(
            self,
            body: disnake.ApplicationCommandInteraction,
            пользователь: disnake.Member = commands.Param(
                description="Участник, который будет верифицирован"
            )
    ):
        role_id = body.guild.get_role(1476451132560773161)
        if role_id not in пользователь.roles:
            пользователь.roles.append(role_id)
            await body.response.send_message(
                f"""
                # :inbox_tray: Верификация
                - Пользователь {пользователь.mention} был верифицирован!
                """,
                delete_after=10
            )
            await пользователь.add_roles(role_id)
        else:
            await body.response.send_message(
                f"""
                # :x: Верификация
                - Пользователь {пользователь.mention} уже верифицирован!
                """,
                delete_after=10
            )
        return

def setup(bot):
    bot.add_cog(VerificationCommand(bot))