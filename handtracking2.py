# HandTrackingModule.py
import mediapipe as mp
import math
import cv2
class HandTracker:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def find_hands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        return results

    def draw_landmarks(self, img, handLms):
        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

    def get_fingers_up(self, handLms):
        return [1 if handLms.landmark[tip].y < handLms.landmark[tip - 2].y else 0 for tip in self.tipIds]

    def get_finger_positions(self, handLms):
        return handLms.landmark[8], handLms.landmark[12]

    def get_finger_distance(self, index_tip, middle_tip):
        return math.hypot(middle_tip.x - index_tip.x, middle_tip.y - index_tip.y)
