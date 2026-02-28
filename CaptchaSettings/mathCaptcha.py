from CaptchaSettings.abstractCaptcha import CaptchaAbstract
import random
import operator

class mathCaptcha(CaptchaAbstract):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    async def captcha_create(self) -> tuple[str, int]:
        num1 = random.randint(4, 15); num2 = random.randint(2, 11)
        symbol = random.choice(list(self.operators.keys()))

        value = self.operators[symbol](num1, num2)
        return f"{num1} {symbol} {num2}", value