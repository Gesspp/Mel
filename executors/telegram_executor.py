from mouse_keyboard_bot import MouseKeyboardBot
from time import sleep

class TelegramExecutor(MouseKeyboardBot):
    def __init__(self, bot: MouseKeyboardBot):
        self.bot = bot


    def find_chat(self, chat_name: str, image):
        self.bot.find(image)
        self.bot.click()
        self.bot.input(chat_name)
        self.bot.click()
        (x, y) = self.bot.get_pos()
        self.bot.sendTo(x, y - 100)
        self.bot.click()

    def hide_telegram(self):
        self.bot.find("./images/main_youtube.PNG")
        self.bot.click()
