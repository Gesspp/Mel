import speech_recognition as sr
import pyttsx3
import os
import subprocess

# Инициализация движка для синтеза речи
engine = pyttsx3.init()

def speak(text):
    """Озвучивание текста"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Распознавание речи"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Вы сказали: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Извините, я не понял.")
        return ""
    except sr.RequestError:
        speak("Ошибка подключения к сервису распознавания.")
        return ""

def execute_command(command):
    """Выполнение системной команды"""
    if "мел" in command or "мяу" in command or "мем" in command:
        if "открой браузер" in command:
            speak("Открываю браузер")
            subprocess.Popen(["c:/Program Files/Google/Chrome/Application/chrome.exe"])  # Например, для Linux
        elif "выключи компьютер" in command:
            speak("Выключаю компьютер")
            os.system("shutdown now")
        elif "папка" in command:
            speak("Открываю домашнюю папку")
            subprocess.Popen(["xdg-open", os.path.expanduser("~")])  # Открытие домашней директории
        elif "создай папку" in command:
            speak("Как назовем папку?")
            folder_name = listen()
            speak(f"создаю папку {folder_name}")
            os.mkdir(folder_name)
        elif "открой steam" in command:
            subprocess.Popen("c:/Program Files (x86)/Steam/steam.exe")
        elif "закрой steam" in command:
            subprocess.Popen.kill("c:/Program Files (x86)/Steam/steam.exe")
        else:
            speak("Команда не распознана")

if __name__ == "__main__":
    while True:
        speak("Слушаю")
        command = listen()
        if command != "отдыхай":
            execute_command(command)
        elif "стоп" in command or "выход" in command or "отдыхай" in command:
            speak("Ушел")
            quit()
            break