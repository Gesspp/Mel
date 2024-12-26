from abc import ABC, abstractmethod
from executors import SystemExecutor, WordExecutor, GoogleSearchExecutor
import speech_recognition as sr
from json import load, dump
import pyttsx3
from errors import ProgramNotFoundError
import pygame



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

    @abstractmethod
    def start(self):
        ...
    
    @abstractmethod
    def get_status(self) -> dict:
        ...

# Инициализация движка для синтеза речи
class Assistant(IAssistant):

    def __init__(
            self, 
            engine: pyttsx3.Engine, 
            recognizer: sr.Recognizer,
            system_executor: SystemExecutor,
            word_executor: WordExecutor,
            search_executor: GoogleSearchExecutor

        ) -> None:
        self.engine = engine
        self.recognizer = recognizer
        self.system_executor = system_executor
        self.word_executor = word_executor
        self.search_executor = search_executor
        self._load_scommands("supercommands.json")

        self.speaking = False
        self.listening = False

        self._keywords = {
            "документ" : self._open_document, 
            "открой" : self.open_router, # done
            "закрой" : self._close_program, # done
            "выключи" : self._shutdown, # done
            "создай папку": self._create_folder, # done
            "громкость" : self._set_volume, # done
            "загугли" : self._search, # done
            "найди": self._youtube_search #todo
        }
        pygame.init()

    def get_status(self) -> dict:
        return {"speaking": self.speaking, "listening": self.listening}

    def get_settings(self) -> dict:
        return {
            "programs" : self.system_executor.programs,
            "sites" : self.search_executor.sites
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
        if not self.speaking:
            self.speaking = True
            self.engine.say(text)
            self.engine.runAndWait()
            self.speaking = False

    def listen(self):
        """Распознавание речи"""
        if not self.listening:
            self.listening = True
            self.play_sound("./sounds/signal.wav")
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            try:
                command = self.recognizer.recognize_google(audio, language="ru-RU") # type: ignore
                print(f"Вы сказали: {command}")
                self.listening = False
                return command.lower()
            except sr.UnknownValueError:
                self.speak("Извините, я не понял.")
                self.listening = False
                return ""
            except sr.RequestError:
                self.speak("Ошибка подключения к сервису распознавания.")
                self.listening = False
                return ""
        return ""

    def set_volume(self, volume: int):
        self.engine.setProperty("volume", volume)

    def delete_program(self, program_name: str):
        self.system_executor.remove_program(program_name)
    def add_program_to_list(self, program_name: str, program_path: str):
        self.system_executor.add_program(program_name, program_path)

    def add_site_to_list(self, site_name: str, site_url: str):
        self.search_executor.add_sites(site_name, site_url)

    def execute_command(self, command: str):
        """Выполнение системной команды"""
        scommands = self._load_scommands("supercommands.json")
        # if "мел" in command or "мяу" in command or "мем" in command:
        for keyword in self._keywords:
            if keyword in command:
                self._keywords[keyword](command)
                return
        for scm in self.scommands.keys():
            if scm.lower() in command:
                self.use_scommand(scm)
                return
        self.speak("Я не знаю такой команды")

    def open_router(self, command: str):
        programs = self.system_executor.programs
        sites = self.search_executor.sites
        command = command.lower()
        value = " ".join(command.split()[1:])
        print(value)

        for program in programs:
            if value == program:
                self.system_executor.execute("open", program)
                self.speak(f"Открываю {program}")
                return
        for site in sites:
            if value == site:
                self.search_executor.open_link(site)
                self.speak(f"Открываю {site}")
                return

        self.speak(f"Я не нашел {value}")


    def _load_scommands(self, config_file: str="supercommands.json"):
        with open(config_file, "r", encoding="utf-8") as file:
            commands = load(file)
            print("Суперкоманды загружены!", commands)
            self.scommands = commands

    def use_scommand(self, command: str):
        print("Использую команду", command)
        subcommands = self.scommands[command]

        for subcommand in subcommands:
            self.execute_command(subcommand)
        

    def _youtube_search(self, command: str):
        querry = command.split()[1:]
        query = " ".join(querry)
        self.search_executor.youtube_search(query)


    def play_sound(self, sound_file="signal.mp3"):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def _search(self, command: str):
        if len(command.split()) < 2:
            self.speak("что ищем?")
            query = self.listen()
        else:
            query = " ".join(command.split()[1:])
        self.search_executor.open_search(query)

    def _open_link(self, command: str):
        if len(command.split()) < 3:
            self.speak("какую ссылку открывать?")
            link = self.listen()
        else:
            link = " ".join(command.split()[2:])
        self.search_executor.open_link(link)

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
    
    
    def _open_document(self, command: str):
        if "открой" in command:
            if len(command.split()) < 3:
                self.speak("как назовем документ?")
                file_name = self.listen()
            else:
                file_name = " ".join(command.split()[2:])
            self.word_executor.execute("open_document", file_name)
            self.speak("открываю документ")
        elif "создай" in command:
            if len(command.split()) < 3:
                self.speak("как назовем документ?")
                file_name = self.listen()
            else:
                file_name = " ".join(command.split()[3:])
            self.word_executor.execute("new_document", file_name)
            self.speak("создал документ")   
        elif "напиши" in command:
            self.speak("Что написать в документ?")
            text = self.listen()
            self.word_executor.execute("new_paragraph", text)
            self.speak("Написал")
        elif "покажи" in command:
            self.speak("Какой документ показать?")
            file_name = self.listen()
            self.word_executor.execute("show_document", file_name)
            self.speak("Показал")
