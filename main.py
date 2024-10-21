from assistant import Assistant
from executors import SystemExecutor, WordExecutor
from mouse_keyboard_bot import MouseKeyboardBot
from keyboard import Keyboard
from sound_changer import SoundChanger
import speech_recognition as sr
import pyttsx3


if __name__ == "__main__":
    bot = MouseKeyboardBot()
    kb = Keyboard()
    sound = SoundChanger(kb)
    sys_exec = SystemExecutor(bot, sound)
    word_exec = WordExecutor()
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    assistant = Assistant(engine, recognizer, sys_exec, word_exec)
    assistant.start()