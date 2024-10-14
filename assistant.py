from abc import ABC, abstractmethod
from executors import SystemExecutor
import speech_recognition as sr
import pyttsx3
from sound import Sound
from errors import ProgramNotFoundError
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# from PyQt5 import QtGui
# import win32com.client as w32
# import wmi
# from yandex_music import Client

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
            sound: Sound,
            system_executor: SystemExecutor
        ) -> None:
        self.engine = engine
        self.recognizer = recognizer
        self.Sound = sound

        self.system_executor = system_executor
        self._keywords = {
            "открой" : self._open_program,
            "закрой" : self._close_program,
            "выключи" : self._shutdown,
            "создай": self._create_folder,
            "громкость" : self._change_volume
        }

    def start(self):
        while True:
            self.speak("Слушаю")
            command = self.listen()
            if "стоп" in command or "выход" in command or "отдыхай" in command:
                self.speak("Ушел")
                return
            self.execute_command(command)

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

    def execute_command(self, command: str):
        """Выполнение системной команды"""
        # if "мел" in command or "мяу" in command or "мем" in command:
        for keyword in self._keywords:
            if keyword in command:
                self._keywords[keyword](command)
                return
        self.speak("Я не знаю такой команды")

    def _open_program(self, command: str):
        try:
            program = " ".join(command.split()[1:])
            self.system_executor.execute("open", program)
            self.speak(f"Открываю {program}")
        except ProgramNotFoundError as e:
            self.speak(str(e))

    def _close_program(self, command: str):
        program = " ".join(command.split()[1:])
        self.system_executor.execute("close", program)
        self.speak(f"закрываю {program}")

    def _shutdown(self):
        self.system_executor.execute("shutdown")

    def _create_folder(self):
        self.speak("как назовем папку?")
        folder_name = self.listen()
        self.system_executor.execute("create_folder", folder_name)

    def _change_volume(self, command: str):
        self.system_executor.execute("change_volume", command.split()[3], True)
    


    # def word_new_document(self):
    #     bot.sendTo(1580, 900)
    #     bot.click()
    #     bot.sendTo(950, 200)
    #     bot.click()

    # def word_print(self):
    #     self.speak("говорите текст")
    #     text = self.listen()
    #     bot.input(text)

    # def return_image(self, program):
    #     directory = os.fsencode("./images")

    #     for el in os.listdir(directory):
    #         filename = os.fsencode(el)
    #         if filename == f"{program[1:]}_close.PNG":
    #             return filename
    #         else:
    #             continue
