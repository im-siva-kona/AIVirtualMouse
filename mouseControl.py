import autopy

class MouseController:
    def __init__(self, screen_size):
        self.wScr, self.hScr = screen_size

    def move_mouse(self, clocX, clocY):
        autopy.mouse.move(self.wScr - clocX, clocY)

    def click(self, button=autopy.mouse.Button.LEFT):
        autopy.mouse.click(button)

    def right_click(self):
        autopy.mouse.click(autopy.mouse.Button.RIGHT)

    def double_click(self):
        # Perform two consecutive left clicks for a double-click effect
        autopy.mouse.click(autopy.mouse.Button.LEFT)
        autopy.mouse.click(autopy.mouse.Button.LEFT)

    def scroll(self, direction):
        autopy.mouse.scroll(direction)
