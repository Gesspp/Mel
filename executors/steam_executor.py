from mouse_keyboard_bot import MouseKeyboardBot
from time import sleep
from utils import get_path

class SteamExecutor:
    def __init__(self, bot: MouseKeyboardBot):
        self.bot = bot

    def find_game(self, game_name: str):
        try:
            self.bot.find(get_path("./images/steam_clear_search.PNG"))
            self.bot.click()
        except:
            pass
        self.bot.find(get_path("./images/steam_find.PNG"))
        self.bot.click()
        sleep(0.2)
        self.bot.input(game_name)
        sleep(0.4)
        (x, y) = self.bot.get_pos()
        self.bot.sendTo(x, y + 60)
        self.bot.click()

    def open_game(self):
        self.bot.find(get_path("./images/steam_open_game.PNG"))
        self.bot.click()
        
    def open(self, game_name: str):
        self.find_game(game_name)
        self.open_game()