import cv2

import mediapipe as mp

import autopy

import time

import math


##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 10
#########################


pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

tipIds = [4, 8, 12, 16, 20]


wScr, hScr = autopy.screen.size()
rectX, rectY, rectW, rectH = 50, 50, 500, 500
rectArea = rectW * rectH
rectSmooth = 10
x3, y3 = 0, 0

# Define regions for specific actions
minimize_region = (rectX, rectY, rectX + rectW // 3, rectY + rectH)
maximize_region = (rectX + rectW // 3, rectY, rectX + 2 * (rectW // 3), rectY + rectH)
close_region = (rectX + 2 * (rectW // 3), rectY, rectX + rectW, rectY + rectH)

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Draw landmarks
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # 2. Get the tip of the index and middle fingers
            index_tip = handLms.landmark[8]
            middle_tip = handLms.landmark[12]

            # 3. Check which fingers are up
            fingers = [1 if handLms.landmark[tip].y < handLms.landmark[tip - 2].y else 0 for tip in tipIds]

            # 4. Only Index Finger: Moving Mode
            if fingers[1] == 1 and fingers[2] == 0:
                # Convert Coordinates
                x3 = int(index_tip.x * wScr)
                y3 = int(index_tip.y * hScr)
                # Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                # Move Mouse
                autopy.mouse.move(wScr - clocX, clocY)
                plocX, plocY = clocX, clocY

            # 8. Both Index and middle fingers are up: Clicking Mode
            elif fingers[1] == 1 and fingers[2] == 1:
                # Find distance between fingers
                length = math.hypot(middle_tip.x - index_tip.x, middle_tip.y - index_tip.y)
                # Click mouse if distance short
                if length < 0.02:
                    autopy.mouse.click()

            # 9. Third finger is up: Right Click
            elif fingers[1] == 0 and fingers[2] == 1:
                autopy.mouse.click(autopy.mouse.Button.RIGHT)
            # 5. Thumb finger up: Double Click
            elif fingers[0] == 1:
                autopy.mouse.click(autopy.mouse.Button.LEFT, 2)  # Double click

            # 6. Index Finger Up, Thumb Finger Open: Scroll Up

    # 5. Draw Rectangle
    cv2.rectangle(img, (rectX, rectY), (rectX + rectW, rectY + rectH), (255, 0, 255), 2)

    # 6. Move Cursor in Rectangle Area
    # Check for specific regions for actions
    if rectX <= clocX <= rectX + rectW and rectY <= clocY <= rectY + rectH:
        if rectX <= clocX <= rectX + rectW // 3:
            autopy.mouse.move(rectX + rectW // 6, rectY + rectH // 2)  # Move to the left region
        elif rectX + rectW // 3 <= clocX <= rectX + 2 * (rectW // 3):
            autopy.mouse.move(rectX + rectW // 2, rectY + rectH // 2)  # Move to the middle region
        else:
            autopy.mouse.move(rectX + 5 * (rectW // 6), rectY + rectH // 2)  # Move to the right region

    cv2.imshow("Image", img)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
