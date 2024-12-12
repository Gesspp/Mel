from assistant import Assistant
from executors import SystemExecutor, WordExecutor, GoogleSearchExecutor
from mouse_keyboard_bot import MouseKeyboardBot
from keyboard import Keyboard
from sound_changer import SoundChanger
import speech_recognition as sr
import pyttsx3
import eel, os


def start_assistant():
    bot = MouseKeyboardBot()
    kb = Keyboard()
    sound = SoundChanger(kb)
    sys_exec = SystemExecutor(bot, sound)
    word_exec = WordExecutor()
    srch_exec = GoogleSearchExecutor()
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    assistant = Assistant(engine, recognizer, sys_exec, word_exec, srch_exec)
    return assistant


eel.init("client")
assist = start_assistant()

@eel.expose
def open_settings():
    eel.start("settings.html", size=(800, 600))


@eel.expose
def run_assistant():
    assist.start()


@eel.expose
def get_status():
    assist.get_status()


@eel.expose
def get_settings():
    return assist.get_settings()


if __name__ == "__main__":
    eel.start("index.html", size=(800, 600))