from abc import ABC, abstractmethod
from executors import SystemExecutor
import speech_recognition as sr
import pyttsx3
from errors import ProgramNotFoundError

class IAssistant(ABC):
    @abstractmethod
    def speak(self, text: str):
        ...

    @abstractmethod
    def listen(self) -> str:
        ...

    @abstractmethod
    def execute_command(self, command: str):
        ...

# Инициализация движка для синтеза речи
class Assistant(IAssistant):

    def __init__(
            self, 
            engine: pyttsx3.Engine, 
            recognizer: sr.Recognizer,
            system_executor: SystemExecutor
        ) -> None:
        self.engine = engine
        self.recognizer = recognizer

        self.system_executor = system_executor
        self._keywords = {
            "открой" : self._open_program, # done
            "закрой" : self._close_program, # done
            "выключи" : self._shutdown, # todo
            "создай": self._create_folder, # done
            "громкость" : self._set_volume # done
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
            command = self.recognizer.recognize_google(audio, language="ru-RU") # type: ignore
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

    def _shutdown(self, command: str):
        self.system_executor.execute("shutdown")

    def _create_folder(self, command: str):
        if len(command.split()) < 3:
            self.speak("как назовем папку?")
            folder_name = self.listen()
        else:
            folder_name = " ".join(command.split()[2:])
        self.system_executor.execute("create_folder", folder_name)
        self.speak(f"создал папку {folder_name}")

    def _set_volume(self, command: str):
        if len(command.split()) < 2:
            self.speak("какую громкость поставить?")
            volume = int(self.listen())
        else:
            volume = int(command.split()[1])
        self.system_executor.execute("set_volume", volume)
    


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
