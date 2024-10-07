from assistant import Assistant
from executors import SystemExecutor
from mouse_keyboard_bot import MouseKeyboardBot
from sound import Sound
import speech_recognition as sr
import pyttsx3


if __name__ == "__main__":
    bot = MouseKeyboardBot()
    sys_exec = SystemExecutor(bot)
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    assistant = Assistant(engine, recognizer, Sound, sys_exec)
    assistant.start()