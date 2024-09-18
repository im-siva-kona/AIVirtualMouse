import cv2
import autopy
from handtracking import HandTracker
from mouseControl import MouseController
import math


wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7


pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

hand_tracker = HandTracker()
mouse_controller = MouseController(autopy.screen.size())

while True:
    success, img = cap.read()
    results = hand_tracker.find_hands(img)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            hand_tracker.draw_landmarks(img, handLms)
            fingers = hand_tracker.get_fingers_status(handLms)
            finger_tips = hand_tracker.get_finger_tips(handLms)

            index_tip, middle_tip = finger_tips

            # Perform mouse actions based on finger positions
            if fingers[1] == 1 and fingers[2] == 0:
                # Only Index Finger: Moving Mode
                x3 = int(index_tip.x * autopy.screen.size()[0])
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                # mouse_controller.move_mouse(clocX, clocY)
                y3 = int(index_tip.y * autopy.screen.size()[1])
                plocX, plocY = clocX, clocY

            elif fingers[1] == 1 and fingers[2] == 1:
                # Both Index and middle fingers are up: Clicking Mode
                mouse_controller.click()



            elif fingers[0] == 1:
                # Both Index and Thumb fingers are up: Double Click
                mouse_controller.double_click()

            elif fingers[1] == 0 and fingers[2] == 1:
                # Three fingers are up: Right Click
                mouse_controller.right_click()

    # Draw Rectangle
    cv2.rectangle(img, (50, 50), (550, 550), (255, 0, 255), 2)

    # Move Cursor in Rectangle Area
    if 50 <= clocX <= 550 and 50 <= clocY <= 550:
        if 50 <= clocX <= 200:
            mouse_controller.move_mouse(100, 300)
        elif 200 < clocX <= 400:
            mouse_controller.move_mouse(300, 300)
        else:
            mouse_controller.move_mouse(500, 300)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
