from assistant import Assistant
from executors import SystemExecutor, WordExecutor
from mouse_keyboard_bot import MouseKeyboardBot
from keyboard import Keyboard
from sound_changer import SoundChanger
import speech_recognition as sr
import pyttsx3, vosk


if __name__ == "__main__":
    bot = MouseKeyboardBot()
    kb = Keyboard()
    sound = SoundChanger(kb)
    sys_exec = SystemExecutor(bot, sound)
    word_exec = WordExecutor()
    engine = pyttsx3.init()
    model_path = 'model/vosk-model-small-ru-0.22' # Замените на путь к модели
    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, 16000)
    assistant = Assistant(engine, recognizer, sys_exec, word_exec)
    assistant.start()