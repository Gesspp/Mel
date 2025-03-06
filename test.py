from mouse_keyboard_bot import MouseKeyboardBot
from executors import TelegramExecutor


if __name__ == "__main__":
    bot = MouseKeyboardBot()
    executor = TelegramExecutor(bot)
    # executor.find_chat("плакса")
    executor.input_message("Почему не работает русский")