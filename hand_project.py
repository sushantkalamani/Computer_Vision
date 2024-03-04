import cv2
import mediapipe as mp
import time 
import HandTrackModule as htm


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,False)
    if len(lmList) != 0:
        thumb_x, thumb_y = lmList[4][1], lmList[4][2]
        index_finger_x, index_finger_y = lmList[8][1], lmList[8][2]

        distance = ((thumb_x - index_finger_x)**2 + (thumb_y - index_finger_y)**2)**0.5
        
        if distance < 30:
            cv2.circle(img, (thumb_x,thumb_y), 15, (0,255,0), cv2.FILLED)
            cv2.circle(img, (index_finger_x,index_finger_y), 10, (0,255,0), cv2.FILLED)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)