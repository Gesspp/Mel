from mouse_keyboard_bot import MouseKeyboardBot
from time import sleep
from utils import get_path


class TelegramExecutor(MouseKeyboardBot):
    def __init__(self, bot: MouseKeyboardBot):
        self.bot = bot


    def find_chat(self, chat_name: str):
        self.bot.switch_to_english()
        sleep(0.5)
        self.bot.find(get_path("images/tg_search_en_white.PNG"))
        self.bot.click()
        sleep(0.2)
        self.bot.input(chat_name)
        sleep(0.4)
        (x, y) = self.bot.get_pos()
        self.bot.sendTo(x, y + 60)
        self.bot.click()

    def hide_telegram(self):
        self.bot.find(get_path("./images/tg_hide.png"))
        self.bot.click()

    def input_message(self, message: str):
        self.bot.find(get_path("./images/tg_input_en_white.PNG"))
        self.bot.click()
        self.bot.input(message)
        sleep(0.2)
        self.bot.find(get_path("./images/tg_send.PNG"))
        self.bot.click()

    def send_message_to(self, chat_name: str, message: str):
        self.find_chat(chat_name)
        self.input_message(message)
