from mouse_keyboard_bot import MouseKeyboardBot
from sound_changer import SoundChanger
from errors import ProgramNotFoundError
from json import load
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

    def _change_volume(self, units: int, is_up: bool=True):
        if is_up:
            self.sound_changer.volume_set(self.sound_changer.current_volume() + units)
        else:
            self.sound_changer.volume_set(self.sound_changer.current_volume() - units)
        
    def _set_volume(self, units: int):
        self.sound_changer.volume_set(units)

    def _load_programs(self, config_file: str="programs.json"):
        with open(config_file, "r") as file:
            programs = load(file)
            print("Программы загружены!", programs)
            self.programs = programs

    def _create_folder(self, folder_name):
        path = (Path.home() / "Desktop" / folder_name)
        path.mkdir()

    def _shutdown(self):
        os.system("shutdown now")