import disnake
from disnake.ext import commands
from CaptchaSettings.mathCaptcha import mathCaptcha
from CaptchaSettings.quizCaptcha import quizCaptcha

class MathematicCaptcha(disnake.ui.Modal):
    def __init__(self, question: str, answer: int):
        self.question = question
        self.answer = answer
        components = [
            disnake.ui.TextInput(
                label=f"Сколько будет {self.question}",
                placeholder="Например: 8",
                custom_id="math_captcha_answer",
                style=disnake.TextInputStyle.short,
                max_length=64,
                min_length=1,
            )
        ]

        super().__init__(
            title="Решите капчу",
            components=components,
        )
    async def callback(self, body: disnake.ModalInteraction):
        try:
            user_answer = int(body.text_values["math_captcha_answer"])
            if user_answer == self.answer:
                role_id = body.guild.get_role(1476451132560773161)
                await body.response.send_message(
                    f"""
                    # :white_check_mark: Вы прошли проверку!
                    \n- Вы ответили правильно ||` {self.question} ` равно ` {self.answer} `||
                    """,
                    ephemeral=True
                )
                await body.author.add_roles(role_id)
            else:
                await body.response.send_message(
                    """
                    # :x: Вы не прошли проверку!
                    \n- Вы ответили неправильно, попробуйте еще раз
                    """,
                    ephemeral=True
                )
            return
        except ValueError:
            await body.response.send_message("# :x: Вы ввели не число!\n- Введите число, чтобы пройти капчу", ephemeral=True)
            return

class QuizCaptcha(disnake.ui.Modal):
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer
        components = [
            disnake.ui.TextInput(
                label=f"{self.question}",
                placeholder="Например: любой текст",
                custom_id="quiz_captcha_answer",
                style=disnake.TextInputStyle.short,
                max_length=45,
                min_length=1,
            )
        ]

        super().__init__(
            title="Решите викторину",
            components=components,
        )
    async def callback(self, body: disnake.ModalInteraction):
        user_answer = body.text_values["quiz_captcha_answer"]
        if self.answer.lower() in user_answer.lower():
            role_id = body.guild.get_role(1476451132560773161)
            await body.response.send_message(
                f"""
                # :white_check_mark: Вы ответили правильно!
                - Вопрос: ` {self.question} `
                - Ответ: ` {self.answer.capitalize()} `
                """,
                ephemeral=True
            )
            await body.author.add_roles(role_id)
        else:
            await body.response.send_message(
                """
                # :x: Неправильный ответ!
                - Попробуйте еще раз, может повезет
                """,
                ephemeral=True
            )
        return

class captcha_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.math = mathCaptcha
        self.quiz = quizCaptcha

    @commands.slash_command(description="Отправьте в чат, чтобы пройти капчу", guild_ids=[1466509350100013226])
    async def captcha(
            self,
            body: disnake.ApplicationCommandInteraction,
            вид_капчи: str = commands.Param(autocomplete=True, description="Вид проверки для прохождения капчи")
    ):
        role_id = body.guild.get_role(1476451132560773161)
        if role_id not in body.author.roles:
            if вид_капчи.lower().startswith("математический"):
                question, answer = await self.math().captcha_create()
                await body.response.send_modal(MathematicCaptcha(question, answer)); return

            if вид_капчи.lower().startswith("любой"):
                question, answer = await self.quiz().captcha_create()
                await body.response.send_modal(QuizCaptcha(question, answer)); return
        else:
            await body.response.send_message(
                """
                # :x: Ошибка
                \n- Вы уже прошли капчу!
                """
            )
            return
        await body.response.send_message(
            """
            # :x: Такого вида капчи нет!
            \n- Выберите доступные варианты
            """,
            ephemeral=True
        )
        return

    @captcha.autocomplete("вид_капчи")
    async def captcha_autocomplete(self, user_input: str):
        captcha_types = ["Математический пример", "Любой вопрос"]
        return [captcha_type for captcha_type in captcha_types if user_input.lower() in captcha_type.lower()[:25]]

def setup(bot):
    bot.add_cog(captcha_command(bot))