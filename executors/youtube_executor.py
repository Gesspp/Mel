from mouse_keyboard_bot import MouseKeyboardBot
from time import sleep

class YoutubeExecutor:
    def __init__(self, bot: MouseKeyboardBot):
        self.bot = bot

    def open_history(self):
        self.bot.find("./images/youtube_history.PNG")
        self.bot.click()

    def open_liked(self):
        self.bot.find("./images/youtube_liked.PNG")
        self.bot.click()
