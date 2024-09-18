# MouseControlModule.py
import autopy

class MouseController:
    def __init__(self, screen_size):
        self.wScr, self.hScr = screen_size

    def move_mouse(self, clocX, clocY):
        autopy.mouse.move(self.wScr - clocX, clocY)

    def click(self, button=autopy.mouse.Button.LEFT, clicks=1):
        autopy.mouse.click(button, clicks=clicks)

    def right_click(self):
        autopy.mouse.click(autopy.mouse.Button.RIGHT)

    def scroll(self, direction):
        autopy.mouse.scroll(direction)
