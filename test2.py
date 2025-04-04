from mouse_keyboard_bot import MouseKeyboardBot
from executors import steam_executor
from time import sleep

bot = MouseKeyboardBot()
executor = steam_executor.SteamExecutor(bot)
executor.open("Dota 2")