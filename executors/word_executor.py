from mouse_keyboard_bot import MouseKeyboardBot

class WordExecutor:
    def __init__(self, bot: MouseKeyboardBot):
        self.bot = bot

    def word_new_document(self):
        self.bot.sendTo(1580, 900)
        self.bot.click()
        self.bot.sendTo(950, 200)
        self.bot.click()

    def word_print(self):
        self.speak("говорите текст")
        text = self.listen()
        self.bot.input(text)