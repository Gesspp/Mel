from mouse_keyboard_bot import MouseKeyboardBot
from sound_changer import SoundChanger
from errors import ProgramNotFoundError
from json import load, dump
from pathlib import Path
import subprocess
import os


class SystemExecutor:
    """Системный исполнитель. Нужен для открытия программ и изменения громкости"""
    def __init__(
            self, 
            bot: MouseKeyboardBot,
            sound_changer_changer: SoundChanger,
            config_file: str="programs.json"
        ):
        self.bot = bot
        self.sound_changer = sound_changer_changer
        self._command_map = {
            "open" : self._open_program,
            "close" : self._close_program,
            "change_volume" : self._change_volume,
            "set_volume" : self._set_volume,
            "create_folder" : self._create_folder,
            "shutdown" : self._shutdown
        }
        self._load_programs(config_file)

    def execute(self, command: str, *args):
        if command not in self._command_map:
            raise Exception(f"Команда {command} не найдена")
        return self._command_map[command](*args)
    

    def _open_program(self, program: str):
        if program not in self.programs.keys():
            raise ProgramNotFoundError(program)
        subprocess.Popen(self.programs[program])

    def _close_program(self, program: str):
        if program not in self.programs.keys():
            raise ProgramNotFoundError(program)
        os.system(f"taskkill /f /im {program}.exe")

    def add_program(self, program_name: str, program_path: str, config_file: str="programs.json"):
        self._load_programs()
        programs = self.programs
        if program_name in programs.keys():
            raise Exception(f"Программа {program_name} уже существует")
        programs[program_name] = program_path
        with open(config_file, "w", encoding="utf-8") as file:
            dump(programs, file, separators=(",\n", ": "))
        self._load_programs()
        

    def remove_program(self, program_name: str, config_file: str="programs.json"):
        with open(config_file, "r", encoding="utf-8") as file:
            programs = load(file)
        with open(config_file, "w", encoding="utf-8") as file:
            del programs[program_name]
            dump(programs, file, separators=(",\n", ": "))
        self._load_programs(config_file)

    def edit_program(self, program_name: str, new_name: str, new_path: str, config_file: str="programs.json"):
        with open (config_file, "r", encoding="utf-8") as file:
            programs = load(file)
        print(programs)
        with open(config_file, "w", encoding="utf-8") as file:
            programs[program_name] = new_path
            if program_name != new_name:
                programs = dict([
                    (key, value) if key != program_name else (new_name, new_path)
                    for key, value in programs.items()
                ])
            print(programs, "после")
            dump(programs, file, separators=(",\n", ": "))


    def _change_volume(self, units: int, is_up: bool=True):
        if is_up:
            self.sound_changer.volume_set(self.sound_changer.current_volume() + units)
        else:
            self.sound_changer.volume_set(self.sound_changer.current_volume() - units)
        
    def _set_volume(self, units: int):
        self.sound_changer.volume_set(units)

    def _load_programs(self, config_file: str="programs.json"):
        with open(config_file, "r", encoding="utf-8") as file:
            programs = load(file)
            print("Программы загружены!", programs)
            self.programs = programs

    def _create_folder(self, folder_name):
        path = (Path.home() / "Desktop" / folder_name)
        path.mkdir()

    def _shutdown(self):
        os.system("shutdown now")