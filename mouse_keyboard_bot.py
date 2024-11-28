import pyautogui as pa
from time import sleep
import pyscreeze

class MouseKeyboardBot: 
    
    def sendTo(self, x, y):
        pa.moveTo(x, y, duration=0)

    def input(self, text):
        pa.write(text)

    def click(self):
        pa.click()

    def get_pos(self):
        (x, y) = pa.position()
        return (x, y)
    
    def find(self, image: str):
        location = pyscreeze.locateOnScreen(image, confidence=0.8)
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