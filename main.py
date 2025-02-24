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

@eel.expose
def add_program(program_name: str, program_path: str):
    assist.add_program_to_list(program_name, program_path)

@eel.expose
def add_site(site_name: str, site_url: str):
    assist.add_site_to_list(site_name, site_url)

@eel.expose
def add_scommand(scommand_name: str, subcommands: list):
    assist.add_scommand_to_list(scommand_name, subcommands)


@eel.expose
def delete_program(program_name: str):
    assist.delete_program(program_name)

@eel.expose
def delete_site(site_name: str):
    assist.delete_site(site_name)

@eel.expose
def delete_scommand(scommand_name: str):
    assist.delete_scommand(scommand_name)

@eel.expose
def edit_program(program_name: str, new_name: str, new_path: str):
    assist.edit_program(program_name, new_name, new_path)

@eel.expose
def set_volume(volume: int):
    assist.set_volume(volume)

if __name__ == "__main__":
    eel.start("index.html", size=(800, 600))