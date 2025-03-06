from mouse_keyboard_bot import MouseKeyboardBot
from time import sleep


class TelegramExecutor(MouseKeyboardBot):
    def __init__(self, bot: MouseKeyboardBot):
        self.bot = bot


    def find_chat(self, chat_name: str):
        self.bot.find("./images/tg_search.PNG")
        self.bot.click()
        self.bot.input(chat_name)
        # self.bot.click()
        # (x, y) = self.bot.get_pos()
        # self.bot.sendTo(x, y - 100)
        # self.bot.click()

    def hide_telegram(self):
        self.bot.find("./images/tg_hide.png")
        self.bot.click()

    def input_message(self, message: str):
        self.bot.find("./images/tg_input.PNG")
        self.bot.click()
        self.bot.input(message)
        sleep(0.5)
        self.bot.find("./images/tg_send.PNG")
        self.bot.click()
