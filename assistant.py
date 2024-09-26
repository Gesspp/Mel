import speech_recognition as sr
import pyttsx3
import os
import subprocess
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from sound import Sound
from json import load
from mouse_keyboard_bot import Bot
# from PyQt5 import QtGui
import win32com.client as w32
import wmi
from yandex_music import Client
from abc import ABC, abstractmethod


class IAssistant(ABC):
    @abstractmethod
    def speak(text: str):
        ...

    @abstractmethod
    def listen():
        ...

    @abstractmethod
    def execute_command(command: str):
        ...

# Инициализация движка для синтеза речи
class Assistant(IAssistant):

    def __init__(
            self, 
            engine: pyttsx3.Engine, 
            recognizer: sr.Recognizer,
            sound: Sound
        ) -> None:
        self.engine = engine
        self.recognizer = recognizer
        self.Sound = sound
        self._load_programs()

    def speak(self, text):
        """Озвучивание текста"""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Распознавание речи"""
        with sr.Microphone() as source:
            print("Слушаю...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Извините, я не понял.")
            return ""
        except sr.RequestError:
            self.speak("Ошибка подключения к сервису распознавания.")
            return ""

    def execute_command(self, command):
        """Выполнение системной команды"""
        # if "мел" in command or "мяу" in command or "мем" in command:
        if "открой" in command.lower():
            program = " ".join(command.split()[1:])
            self._open_program(program)
        elif "закрой" in command.lower():
            program = " ".join(command.split()[1:])
            self._close_program(program)
        elif "выключи компьютер" in command:
            self.speak("Выключаю компьютер")
            os.system("shutdown now")
        elif "папка" in command:
            self.speak("Открываю домашнюю папку")
            subprocess.Popen(["xdg-open", os.path.expanduser("~")])
        elif "создай папку" in command:
            self.speak("Как назовем папку?")
            folder_name = self.listen()
            self.speak(f"создаю папку {folder_name}")
            os.mkdir(folder_name)
        elif "повысь громкость" in command:
            self._change_volume(command.split()[3], True)
        elif "создай документ" in command:
            self.word_new_document()
        elif "печатай" in command:
            self.word_print()
        else:
            pass

    def _open_program(self, program):
        if program not in self.programs.keys():
            self.speak("Я не знаю такой программы. Проверьте файл \"programs.json\"")
            return
        self.speak(f"Открываю {program}")
        subprocess.Popen(self.programs[program])

    def word_new_document(self):
        bot.sendTo(1580, 900)
        bot.click()
        bot.sendTo(950, 200)
        bot.click()

    def _close_program(self, program):
        if program not in self.programs.keys():
            self.speak("Я не знаю такой программы. Проверьте файл \"programs.json\"")
            return
        self.speak(f"закрываю {program}")
        image = self.return_image(program)
        bot.find(image)
        bot.click()

    def _change_volume(self, units: int, is_up: bool=True):
        if is_up:
            self.Sound.volume_set(self.Sound.current_volume() + int(units))
        else:
            self.Sound.volume_set(self.Sound.current_volume() - int(units))
        
    def _set_volume(self, units: int):
        self.Sound.volume_set(int(units))

    def _load_programs(self, config_file: str="programs.json"):
        with open(config_file, "r") as file:
            programs = load(file)
            print("Программы загружены!", programs)
            self.programs = programs

    def word_print(self):
        self.speak("говорите текст")
        text = self.listen()
        bot.input(text)

    def return_image(self, program):
        directory = os.fsencode("./images")

        for el in os.listdir(directory):
            filename = os.fsencode(el)
            if filename == f"{program[1:]}_close.PNG":
                return filename
            else:
                continue

if __name__ == "__main__":
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    assistant = Assistant(engine, recognizer, Sound)
    bot = Bot(int, int, str)
    client = Client()
    client.init()
    # assistant._change_volume(10, False)
    while True:
        assistant.speak("Слушаю")
        command = assistant.listen()
        if command != "отдыхай":
            assistant.execute_command(command)
        elif "стоп" in command or "выход" in command or "отдыхай" in command:
            assistant.speak("Ушел")
            quit()
            break