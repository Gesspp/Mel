import pyautogui as pa
import keyboard
from time import sleep
from pyperclip import copy, paste
import pyscreeze
import ctypes

class MouseKeyboardBot: 
    def switch_to_english(self):
        """Принудительно меняет раскладку на английскую"""
        HWND = ctypes.windll.user32.GetForegroundWindow()
        ctypes.windll.user32.PostMessageW(HWND, 0x50, 0, 0x4090409)



    def sendTo(self, x, y):
        pa.moveTo(x, y, duration=0.5)

    def input(self, text):
        copy(text)
        sleep(0.3)
        keyboard.press_and_release('ctrl+v')

    def click(self):
        pa.click()

    def get_pos(self):
        (x, y) = pa.position()
        return (x, y)
    
    def find(self, image: str):
        location = pyscreeze.locateOnScreen(image, confidence=0.7)
        pa.moveTo(location)

    def find_rounded(self, image: str):
        location = pyscreeze.locateOnScreen(image, confidence=0.8)
        coords = []
        while location != (0, 0):
            coords.append(location)
            location = pyscreeze.locateOnScreen(image, confidence=0.8)
        return coords


# mb = MouseKeyboardBot()
# sleep(4)
# mb.find_rounded("./images/youtube_video_lock.PNG")
# mb.click()