import pyautogui as pa

class MouseKeyboardBot:
    def __init__(self, x: int, y: int, text: str) -> None:
        self.x = x
        self.y = y
        self.text = text
    
    def sendTo(self, x, y):
        pa.moveTo(x, y, duration=0)

    def input(self, text):
        pa.write(text)

    def click(self):
        pa.click()
    
    def find(self, image: str):
        location = pa.locateCenterOnScreen(image)
        pa.moveTo(location)