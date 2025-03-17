from mouse_keyboard_bot import MouseKeyboardBot
from executors import TelegramExecutor
from time import sleep


if __name__ == "__main__":
    bot = MouseKeyboardBot()
    executor = TelegramExecutor(bot)
    # executor.find_chat("Александр Алексеевич Про")
    # sleep(0.5)
    executor.send_message_to("Александр Алексеевич Про", "Почему не работает русский")