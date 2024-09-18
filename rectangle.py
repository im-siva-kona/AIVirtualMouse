import autopy
import cv2

class RectangleDrawer:
    def __init__(self, rect_params):
        self.rectX, self.rectY, self.rectW, self.rectH = rect_params

    def draw_rectangle(self, img):
        cv2.rectangle(img, (self.rectX, self.rectY), (self.rectX + self.rectW, self.rectY + self.rectH), (255, 0, 255), 2)

    def move_cursor_in_rectangle(self, mouse_controller, clocX, clocY):
        # Check if the cursor is within the defined rectangle
        if self.rectX <= clocX <= self.rectX + self.rectW and self.rectY <= clocY <= self.rectY + self.rectH:
            # Implement your logic for cursor movement within the rectangle
            # Example: Move to the center of the rectangle
            center_x = self.rectX + self.rectW // 2
            center_y = self.rectY + self.rectH // 2
            mouse_controller.move_mouse(center_x, center_y)
