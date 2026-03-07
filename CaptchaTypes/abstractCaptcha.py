from abc import ABC, abstractmethod

class CaptchaAbstract(ABC):
    @abstractmethod
    def captcha_create(self):
        pass